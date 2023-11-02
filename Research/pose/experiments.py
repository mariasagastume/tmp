"""
Run experiments and reconstruct pose estimates from reciprocal representations.
"""
import logging
import numpy as np
import numpy.typing as npt
import scipy
from scipy.sparse import csr_array
from sklearn.cluster import DBSCAN

import nengo
import nengo_loihi
from nengo.processes import Piecewise
# from nengo_extras.plot_spikes import plot_spikes

from pose.freq_space import (
    flatten_coefs,
    unflatten_coefs,
    ifftn_hex,
    get_0_coefs
)
from pose.hex import (
    get_3d_distances_unwrapped,
    get_domain,
    get_3d_distances,
    unwrap_multi,
    fspace_base,
    inv_fspace_base,
    get_3d_coordinates_unwrapped,
    wrap_closer,
    wrap_into_parallelogram
)
from pose.io_utils import get_mem_info
from pose.input import (
    cmd_list_to_inhib_values,
    preprocess_input_list
)
from pose.nengo_utils import (
    get_weights_optimized,
    get_pose_network,
    get_encoders
)
from pose.typing import GridShape


logger = logging.getLogger(__name__)


def run_experiment(
    _config: dict
) -> dict:
    """Runs a simulation for the given config dict.
    Computes the connection weights, sets up the pose network, prepares the input, runs the
    simulation, and constructs an output dict.

    Args:
        _config: Dict of parameters for the network setup, simulation, etc.
                 (see `exp.default_config` for supported config parameters and sensible defaults)

    Returns:
        Dict of recorded simulation data.
    """
    # parse config
    dt = _config['dt']

    simulation_duration = _config['simulation_duration']
    seed = _config['seed']
    np.random.seed(seed)
    # random.seed(seed)
    nengo_seed = _config['nengo_seed']

    variance_pose = _config['variance_pose']
    cov = np.eye(3) * variance_pose
    grid_shape = _config['grid_shape']
    assert(grid_shape[0] == grid_shape[1])  # ensure that x and y are equal -> needs to form equilateral triangle/rhombus
    fgrid_shape = _config['fgrid_shape']  # here x and y also need to be equal
    tau = _config['tau']
    sample_every = _config['sample_every']
    weight_config = _config['weights']
    weight_sparse_threshold = _config['weight_sparse_threshold']
    use_loihi = _config['use_loihi']

    # compute connection weights according to weight_config
    rec_con_weights, shift_weights, pos_rot_weights, neg_rot_weights = get_weights_optimized(grid_shape, weight_config)

    rec_con_weights[np.abs(rec_con_weights) < weight_sparse_threshold] = 0
    shift_weights[np.abs(shift_weights) < weight_sparse_threshold] = 0
    pos_rot_weights[np.abs(pos_rot_weights) < weight_sparse_threshold] = 0
    neg_rot_weights[np.abs(neg_rot_weights) < weight_sparse_threshold] = 0

    rec_con_weights = csr_array(rec_con_weights)
    shift_weights = csr_array(shift_weights)
    pos_rot_weights = csr_array(pos_rot_weights)
    neg_rot_weights = csr_array(neg_rot_weights)

    # set up the pose network
    kwargs = {'seed': nengo_seed}

    pose_network = get_pose_network(
        grid_shape,
        fgrid_shape,
        cov,
        tau,
        dt,
        rec_con_weights=rec_con_weights,  # sim_weights2/sim_gains2
        shift_con_weights=shift_weights,  # eval_point_targets[:, encoding_mask(fgrid_shape).ravel()],
        rot_con_weights_pos=pos_rot_weights,
        rot_con_weights_neg=neg_rot_weights,
        _config=_config,
        label='pose_network',
        seed=kwargs.setdefault('seed', 0))

    # prepare input
    encoders, scale_fact = get_encoders(grid_shape, fgrid_shape, cov)
    gauss0_f_cropped_flat = get_0_coefs(fgrid_shape, cov)
    cmds = _config['input']

    import copy
    cmds_prep = copy.deepcopy(cmds)
    preprocess_input_list(cmds_prep)
    input_provider = cmd_list_to_inhib_values(cmds_prep, fgrid_shape, gauss0_f_cropped_flat, encoders, scale_fact)

    input_dict = {}
    time_array = get_time_array(cmds_prep)
    for index in range(time_array.shape[0]):
        t = time_array[index, 0]
        cur_input = input_provider(t)
        reset_input = cur_input['input']
        if 'tangential_vel' in cur_input.keys():
            tangential_velocity = cur_input['tangential_vel']
            angular_velocity = cur_input['angular_vel']
        else:
            # TODO: maybe update with fitted vel-inhib relation
            tangential_velocity = 1 - max(0, cur_input['shift_inhib'])
            angular_velocity = cur_input['neg_rot_shift_inhib'] - cur_input['pos_rot_shift_inhib']
        input_dict[t] = np.concatenate((reset_input, np.atleast_1d(tangential_velocity), np.atleast_1d(angular_velocity)))

    input_process = Piecewise(input_dict)

    with pose_network:
        final_input = nengo.Node(input_process, size_out=input_process.default_size_out, label='process_input')
        nengo.Connection(final_input, pose_network.input, synapse=None, label='process_input_con')

    # define output via probes
    probe_dict = {
        'pose_network.output': None  # pose representation in reciprocal space
        # 'pose_network.shift_inhib.output': None,
        # 'pose_network.ccw_rot_inhib.output': None,
        # 'pose_network.cw_rot_inhib.output': None,
        # 'pose': [],
        # 'pose.input': [],
        # 'pose.decoded_output': [],
        # 'pose.scaled_encoders': [],
        # 'pose.neurons.input': [],
        # 'pose.neurons.output': [],
        # 'pose.neurons.voltage': [],
        # 'rec_con.output': []
    }

    with pose_network:
        probe_dict['pose_network.output'] = nengo.Probe(pose_network.output, sample_every=sample_every, synapse=0.01)
        # probe_dict['pose_network.shift_inhib.output'] = nengo.Probe(pose_network.shift_inhib, attr='output', sample_every=sample_every, synapse=None)

    # build simulation
    logger.info('build simulation' + get_mem_info())
    if use_loihi:
        sim = nengo_loihi.Simulator(pose_network, dt, hardware_options={"snip_max_spikes_per_step": 400})
        # print("\n".join(sim.model.utilization_summary()))
    else:
        sim = nengo.Simulator(pose_network, dt)

    # run simulation
    logger.info('run simulation' + get_mem_info())
    try:
        sim.run(simulation_duration)
    finally:
        sim.close()

    # construct output dict
    logger.info('store results' + get_mem_info())
    data = {}
    for key in probe_dict:
        if probe_dict[key] is not None:
            data[key] = sim.data[probe_dict[key]]

    return data


def reconstruct_timeseries(
    data: npt.NDArray[np.float64],
    fgrid_shape: GridShape
) -> npt.NDArray[np.float64]:
    """Reconstructs the real-space representation for each time step from the respective flattened
    Fourier coefficient vector.

    Args:
        data: Array of flattened Fourier coefficient vectors as e.g. decoded from a Nengo
              simulation.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        Array of three-dimensional snapshots of the real-space pose domain.
    """

    num_timepoints = data.shape[0]
    est = np.zeros((num_timepoints, *fgrid_shape))

    for t in range(num_timepoints):
        # NOTE: could use reconstructions of previous timepoints to
        #       influence the current reconstruction
        fourier_coefs = unflatten_coefs(data[t], fgrid_shape)
        est[t] = ifftn_hex(fourier_coefs)

    return est


def get_cluster_centers(
    data: npt.NDArray[np.float64],
    coords_freq_space: npt.NDArray[np.float64],
    dist_mat: npt.NDArray[np.float64],
    threshold: np.float64 = 0.4
) -> npt.NDArray[np.float64]:
    """Computes the pose estimates from a snapshot of the real-space pose domain sampled at
    discrete points.
    The number of pose estimates is variable and may even be zero. Data points are separated via
    clustering. Each pose estimate is then obtained as weighted average of the points in it's
    cluster.

    Args:
        data: Sampled real-space pose volume. Shape ``(*grid_shape)``.
        coords_freq_space: Coordinates in reciprocal space corresponding to the real-space sample
                           points.
        dist_mat: Matrix of pairwise distances between the sample points in real space.
        threshold: Fraction of the maximum value in the input data that points need to have in order
                   to be considered for clustering.

    Returns:
        Array of pose estimates.
    """
    res_x = data.shape[0]

    # indexing mask to select points for clustering
    cur_max = data.max()
    idx = data > (cur_max * threshold)

    dist_mat_filtered = dist_mat[idx.flatten(), :]
    dist_mat_filtered = dist_mat_filtered[:, idx.flatten()]

    eps = 1/res_x*1.1  # TODO: maybe add arg
    try:
        db = DBSCAN(eps=eps, metric='precomputed').fit(dist_mat_filtered, sample_weight=data[idx])
        num_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
    except Exception as e:
        print(e)
        num_clusters = 0

    cluster_centers = np.empty((num_clusters, 3))

    # compute the cluster centers from the clustered points
    for c in range(num_clusters):
        cluster_data = data[idx][db.labels_ == c]
        cluster_points = coords_freq_space[idx][db.labels_ == c]
        if cluster_points.shape[0] > 1:
            cluster_points_wrapped_closer = np.vstack((cluster_points[0].reshape(
                (1, -1)), wrap_closer(cluster_points[0], cluster_points[1:])))
        else:
            cluster_points_wrapped_closer = cluster_points
        cluster_points_wrapped_closer_time_space = cluster_points_wrapped_closer.dot(fspace_base.transpose())
        cluster_center_prelim = np.average(cluster_points_wrapped_closer_time_space, weights=cluster_data, axis=0)

        cluster_center_prelim_freq_space = inv_fspace_base.dot(cluster_center_prelim)
        cluster_center_freq_space = wrap_into_parallelogram(cluster_center_prelim_freq_space)
        cluster_centers[c] = fspace_base.dot(cluster_center_freq_space)

        # just take middle value of cluster's points
        # approx_center_idx = np.sum(db.labels_ == c) // 2
        # cluster_centers[c] = coords[idx][db.labels_ == c][approx_center_idx]

        # old wrap-around:
        # print(cluster_centers[c])
        # dists_label0 = np.stack(get_3d_distances_unwrapped(fourier_coef_shape), axis=-1)[0, idx.flatten(), :][db.labels_==c, :]
        # # wrap around so that all values are positive  FIXME: potential bug: 0.5 in x only if neg wrap in y
        # print(dists_label0)
        # dists_label0[:,0][np.logical_and(dists_label0[:,0] < 0, np.logical_not(dists_label0[:,1] < 0))] = dists_label0[:,0][np.logical_and(dists_label0[:,0] < 0, np.logical_not(dists_label0[:,1] < 0))] + 1
        # dists_label0[:,0][np.logical_and(dists_label0[:,0] < 0, dists_label0[:,1] < 0)] = dists_label0[:,0][np.logical_and(dists_label0[:,0] < 0, dists_label0[:,1] < 0)] + 0.5
        # # dists_label0[:,0][dists_label0[:,0] < 0] = dists_label0[:,0][dists_label0[:,0] < 0] + 0.5
        # dists_label0[:,1][dists_label0[:,1] < 0] = dists_label0[:,1][dists_label0[:,1] < 0] + sqrt(3)/2
        # dists_label0[:,2][dists_label0[:,2] < 0] = dists_label0[:,2][dists_label0[:,2] < 0] + 1
        # print(dists_label0)
        # approx_center = np.mean(dists_label0, axis=0)

    return cluster_centers


def get_cluster_centers_timeseries(
    data: npt.NDArray[np.float64],
    fgrid_shape: GridShape
):
    """Computes the pose estimates for multiple time points, each given as real-space pose volume
    sampled at a hexagonal grid.
    The number of pose estimates may be different for each time point.

    Args:
        data: Array of sampled real-space pose volumes.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        List of array of pose estimates.
    """
    num_timepoints = data.shape[0]

    cluster_centers = []
    # est = np.zeros((num_timepoints, max_num_bumps, 3))
    # num_bumps = np.zeros(num_timepoints)

    fgenerators = fspace_base / np.array(fgrid_shape)
    coords = get_3d_coordinates_unwrapped(fgrid_shape, fgenerators)
    coords_freq_space = coords.dot(inv_fspace_base.transpose())
    dist_mat = np.linalg.norm(np.stack(get_3d_distances_unwrapped(fgrid_shape), axis=-1), axis=-1)

    for t in range(num_timepoints):
        cluster_centers.append(get_cluster_centers(data[t], coords_freq_space, dist_mat))
        # num_bumps[t] = cluster_centers.shape[0]
        # est[t, :num_bumps[t]] = cluster_centers

    return cluster_centers


def get_time_array(
    input: list[dict]
) -> npt.NDArray[np.float64]:
    """Computes the start and stop time points for a list of input commands with individual
    durations.

    Args:
        input: List of input commands.

    Returns:
        Array of start and stop time points.
    """
    time_array = np.empty((len(input), 2))
    cur_time = 0

    for index, cmd_block in enumerate(input):
        next_time = round(cur_time + cmd_block['duration'], 8)
        time_array[index] = [cur_time, next_time]
        cur_time = next_time

    return time_array


def get_naive_pose_est_abelian(data, fourier_generators):
    """Get a single pose estimate per time point as the location of the maximum value in the
    respective sampled three-dimensional pose volume.

    Notes:
        Deprecated.
    """
    num_levels = data.shape[0]
    num_timepoints = data.shape[1]

    num_dims = 3  # x, y, theta
    est_idx = np.zeros((num_levels, num_timepoints, num_dims))
    est = np.zeros((num_levels, num_timepoints, num_dims))

    for i in range(num_levels):
        for t in range(num_timepoints):
            gauss = data[i, t]  # .reshape((Nu, Nv, Nw))

            approx_max = np.argmax(gauss)
            out = np.unravel_index(approx_max, gauss.shape)
            out = np.asarray(out)

            est_idx[i, t] = out
            est[i, t] = fourier_generators.dot(out)

    return est_idx, est


def get_gauss_freq_optimized(grid_shape):
    """Returns a function that shifts a given vector of Fourier coefficients by a given displacement
    vector in three-dimensional frequency space. Uses a rotation matrix.

    Notes:
        Deprecated.
    """
    def gauss(x, meanx, meany, meanz):  # TODO: include a factor?
        center = get_domain() * np.array([meanx, meany, meanz])
        rot_mat = rot_mat_cropped_abelian(grid_shape, center, crop_conj_sym=False)
        C_rotated = rot_mat.dot(x)

        return C_rotated.ravel()

    return gauss


def get_gauss_pose_est_freq_optimized(data, grid_shape, initial_guesses_mean, initial_guess_var):
    """For each time point, fits a *single* three-dimensional Gaussian (`get_gauss_freq_optimized`)
    to the respective discretized pose volume and estimates the current pose as the Gaussian's mean.
    For efficiency, the function fitting is done purely in frequency space.

    Notes:
        Deprecated.
    """

    num_levels = data.shape[0]
    num_timepoints = data.shape[1]

    num_dims = 3  # x, y, theta
    est = np.zeros((num_levels, num_timepoints, num_dims))

    # u_diff, v_diff, w_diff = hex_utils.get_3d_distances(*grid_shape)
    # pos = np.stack((u_diff[0], v_diff[0], w_diff[0]), axis=-1)
    u_diff, v_diff, w_diff = get_3d_distances(grid_shape)
    u_diff_unwrapped = unwrap_multi(u_diff.reshape((*grid_shape, *grid_shape)), grid_shape,
                                    1).reshape((np.prod(grid_shape), np.prod(grid_shape)))
    v_diff_unwrapped = unwrap_multi(v_diff.reshape((*grid_shape, *grid_shape)), grid_shape,
                                    1).reshape((np.prod(grid_shape), np.prod(grid_shape)))
    w_diff_unwrapped = unwrap_multi(w_diff.reshape((*grid_shape, *grid_shape)), grid_shape,
                                    1).reshape((np.prod(grid_shape), np.prod(grid_shape)))
    pos = np.stack((u_diff_unwrapped[0], v_diff_unwrapped[0], w_diff_unwrapped[0]), axis=-1)

    var = initial_guess_var
    cov = var * np.eye(3)

    Z = scipy.stats.multivariate_normal.pdf(x=pos, mean=np.zeros(3), cov=cov).reshape(grid_shape)
    C_computed = np.fft.fftn(Z, s=grid_shape, norm='forward') * np.prod(get_domain())
    C_computed = remove_nyquist(flatten_coefs(C_computed), grid_shape, crop_conj_sym=False)

    for i in range(num_levels):
        for t in range(num_timepoints):
            cur_data = data[i, t]

            initial_guess_mean = inv_fspace_base.dot(initial_guesses_mean[i, t])
            initial_guess = (*initial_guess_mean,)

            popt, _ = scipy.optimize.curve_fit(
                get_gauss_freq_optimized(grid_shape),
                xdata=C_computed,
                ydata=cur_data.ravel(),
                p0=initial_guess,
                bounds=([-0.1, -0.1, -0.1], [1.1, 1.1, 1.1]), ftol=5e-3, xtol=5e-3)  # TODO: maybe adapt ftol and xtol when using higher grid resolution

            est[i, t] = popt[:3]

            if est[i, t][0] < 0:
                est[i, t][0] = est[i, t][0] + 1
            elif est[i, t][0] > 1:
                est[i, t][0] = est[i, t][0] - 1
            if est[i, t][1] < 0:
                est[i, t][1] = est[i, t][1] + 1
            elif est[i, t][1] > 1:
                est[i, t][1] = est[i, t][1] - 1
            if est[i, t][2] < 0:
                est[i, t][2] = est[i, t][2] + 1
            elif est[i, t][2] > 1:
                est[i, t][2] = est[i, t][2] - 1

            # if t > 0:
            #     est[i, t] = 0.8 * est[i, t] + 0.2 * est[i, t-1]

            est[i, t] = fspace_base.dot(est[i, t])

    return est


def get_gauss_freq2(grid_shape):
    """Returns a function that computes the vector of Fourier coefficients corresponding to two
    three-dimensional Gaussians given by their mean, variance and scaling factor. Uses rotation
    matrices.

    Notes:
        Deprecated.
    """
    # TODO: include a factor? -> probably necessary since want to know which bump is dominant currently
    def gauss(x, meanx, meany, meanz, var, fact, meanx2, meany2, meanz2, var2, fact2):
        # bump 1
        cov = var * np.eye(3)

        Z = scipy.stats.multivariate_normal.pdf(x=x, mean=np.zeros(3), cov=cov).reshape(grid_shape)
        Z = Z * fact
        C_computed = np.fft.fftn(Z, s=grid_shape, norm='forward') * np.prod(get_domain())
        C_computed = remove_nyquist(flatten_coefs(C_computed), grid_shape, crop_conj_sym=False)

        center = get_domain() * np.array([meanx, meany, meanz])
        rot_mat = rot_mat_cropped_abelian(grid_shape, center, crop_conj_sym=False)
        C_rotated = rot_mat.dot(C_computed)

        # bump 2
        cov2 = var2 * np.eye(3)

        Z2 = scipy.stats.multivariate_normal.pdf(x=x, mean=np.zeros(3), cov=cov2).reshape(grid_shape)
        Z2 = Z2 * fact2
        C_computed2 = np.fft.fftn(Z2, s=grid_shape, norm='forward') * np.prod(get_domain())
        C_computed2 = remove_nyquist(flatten_coefs(C_computed2), grid_shape, crop_conj_sym=False)

        center2 = get_domain() * np.array([meanx2, meany2, meanz2])
        rot_mat2 = rot_mat_cropped_abelian(grid_shape, center2, crop_conj_sym=False)
        C_rotated2 = rot_mat2.dot(C_computed2)

        C_final = C_rotated + C_rotated2

        return C_final.ravel()

    return gauss


def get_gauss_pose_est_freq2(data, grid_shape, num_bumps, initial_guesses_mean, initial_guess_var):
    """For each time point, fits two individually-scaled three-dimensional Gaussians
    (`get_gauss_freq2`) to the respective discretized pose volume and estimates *up to two* current
    poses as the Gaussians' means. The function fitting is done real space.

    Notes:
        Deprecated.
    """
    # estimate shift in unscaled frequency space (i.e. not scaled by the domain)
    num_levels = data.shape[0]
    num_timepoints = data.shape[1]

    num_dims = 3  # x, y, theta
    est = np.zeros((num_levels, num_timepoints, 2*num_dims+4))

    u_diff_unwrapped, v_diff_unwrapped, w_diff_unwrapped = get_3d_distances_unwrapped(grid_shape)
    pos = np.stack((u_diff_unwrapped[0], v_diff_unwrapped[0], w_diff_unwrapped[0]), axis=-1)

    for i in range(num_levels):
        for t in range(num_timepoints):
            cur_data = data[i, t]

            cur_num_bumps = int(num_bumps[i, t])

            initial_guess_mean = inv_fspace_base.dot(
                initial_guesses_mean[i, t, :cur_num_bumps].transpose()).transpose()
            initial_guess = (*initial_guess_mean[0], initial_guess_var, 0.2,
                             *initial_guess_mean[1], initial_guess_var, 0.2)

            popt, _ = scipy.optimize.curve_fit(
                get_gauss_freq2(grid_shape),
                xdata=pos,
                ydata=cur_data.ravel(),
                p0=initial_guess,
                bounds=([initial_guess_mean[0, 0] - 0.3, initial_guess_mean[0, 1] - 0.3, initial_guess_mean[0, 2] - 0.3, 0.0045, 0.1, initial_guess_mean[1, 0] - 0.3, initial_guess_mean[1, 1] - 0.3, initial_guess_mean[1, 2] - 0.3, 0.0045, 0.1], [initial_guess_mean[0, 0] + 0.3, initial_guess_mean[0, 1] + 0.3, initial_guess_mean[0, 2] + 0.3, 0.008, 0.6, initial_guess_mean[1, 0] + 0.3, initial_guess_mean[1, 1] + 0.3, initial_guess_mean[1, 2] + 0.3, 0.008, 0.6]), ftol=5e-3, xtol=5e-3)  # TODO: maybe adapt ftol and xtol when using higher grid resolution

            est[i, t] = popt
            # est[i, t, 0:3] = popt[:3]
            # est[i, t, 3:6] = popt[4:7]
            # est[i, t, 6] = popt[8]

            if est[i, t][0] < 0:
                est[i, t][0] = est[i, t][0] + 1
            elif est[i, t][0] > 1:
                est[i, t][0] = est[i, t][0] - 1
            if est[i, t][1] < 0:
                est[i, t][1] = est[i, t][1] + 1
            elif est[i, t][1] > 1:
                est[i, t][1] = est[i, t][1] - 1
            if est[i, t][2] < 0:
                est[i, t][2] = est[i, t][2] + 1
            elif est[i, t][2] > 1:
                est[i, t][2] = est[i, t][2] - 1

            if est[i, t][5] < 0:
                est[i, t][5] = est[i, t][5] + 1
            elif est[i, t][5] > 1:
                est[i, t][5] = est[i, t][5] - 1
            if est[i, t][6] < 0:
                est[i, t][6] = est[i, t][6] + 1
            elif est[i, t][6] > 1:
                est[i, t][6] = est[i, t][6] - 1
            if est[i, t][7] < 0:
                est[i, t][7] = est[i, t][7] + 1
            elif est[i, t][7] > 1:
                est[i, t][7] = est[i, t][7] - 1

            # if t > 0:
            #     est[i, t] = 0.8 * est[i, t] + 0.2 * est[i, t-1]

            est[i, t, 0:3] = fspace_base.dot(est[i, t, 0:3])
            est[i, t, 5:8] = fspace_base.dot(est[i, t, 5:8])

    return est
