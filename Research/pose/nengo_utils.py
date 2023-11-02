"""
Define the entire pose network as a Nengo structure, including encoders and connection weights.
"""
import logging
from math import pi
import nengo
# from nengo_extras.neurons import FastLIF
import nengo_loihi
import numpy as np
import numpy.typing as npt
from scipy.sparse import csr_array, identity
from scipy.stats import multivariate_normal

import pose
from pose.io_utils import (
    get_mem_info
)
import pose.input
from pose.freq_space import (
    get_rotation_matrix,
    get_0_coefs,
    unflatten_coefs,
    get_nyquist_mask,
    flatten_coefs
)
from pose.hex import (
    get_domain,
    get_3d_distances_unwrapped,
    polar_to_cartesian,
    inv_fspace_base
)
from pose.typing import GridShape


logger = logging.getLogger(__name__)


init_period = 1.0


# def getf_global_inhib(dt):
#     """Wrapper function which returns the function which provides global
#     inhibitory input."""

#     def global_inhib(t):
#         """Provides inhibitory input to the pose ensemble at time t."""

#         out = 0.0

#         interval_speed = 1  # semi-constant when interval_speed > 1

#         if (t >= init_period) and (abs((t/dt) % interval_speed) < 1e-5):
#             # out = 1.4  # * 2.0
#             out = 0.01
#         else:
#             1

#         return out

#     return global_inhib


# returns True if cur is active at t, False otherwise
# cur is 0 or 1
# def split_time(t, dt, cur):
#     if abs((t/dt) % 2) - cur < 1e-5:
#         return True
#     else:
#         return False


def mex_hat(
    x: npt.ArrayLike,
    var_exc: np.float64,
    var_inh: np.float64,
    fact_exc: np.float64,
    fact_inh: np.float64,
    offset: np.float64
) -> npt.NDArray[np.float64]:
    """Computes a mexican hat function at the specified locations.

    Args:
        x: Points for evaluating the Gaussians.
        var_exc: Variance of the excitatory Gaussian.
        var_inh: Variance of the inhibitory Gaussian.
        fact_exc: Scaling factor of the excitatory Gaussian.
        fact_inh: Scaling factor of the inhibitory Gaussian.
        offset: Constant global offset.

    Returns:
        Function values.
    """
    cov_exc = var_exc * np.eye(3)
    Z = multivariate_normal.pdf(x=x, mean=np.zeros(3), cov=cov_exc)
    Z = Z * fact_exc

    cov_inh = var_inh * np.eye(3)
    Z2 = multivariate_normal.pdf(x=x, mean=np.zeros(3), cov=cov_inh)
    Z2 = Z2 * fact_inh

    Z_final = Z - Z2 - offset

    return Z_final.ravel()


def encoding_len(
    fgrid_shape: GridShape
) -> int:
    """Computes the final number of representational dimensions based on the index mask.

    Args:
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        Number of representational dimensions.
    """
    return encoding_mask(fgrid_shape).sum()


def encoding_mask(
    fgrid_shape: GridShape
) -> npt.NDArray[np.float64]:
    """Generates an indexing mask for the flattened Fourier coefficient vector to exclude certain
    dimensions, e.g. the imaginary part of the Nyquist terms.

    Args:
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        Flat index mask.
    """
    # mask = np.ones(fgrid_shape, dtype=bool)
    # # mask[0, 0, 0] = 0  # omit first Fourier coefficient
    # mask_flat = np.stack((mask, mask), -1)  # duplicate mask since separate real and imag parts
    # mask_flat[0, 0, 0, 0] = 0  # omit real part of first Fourier coefficient
    # mask_flat[0, 0, 0, 1] = 0  # omit imaginary part of first Fourier coefficient

    mask_flat = get_nyquist_mask(fgrid_shape)
    # mask_flat[0] = 0

    return mask_flat


def rotate_to_grid(
    coefs: npt.NDArray[np.float64],
    grid_shape: GridShape,
    fgrid_shape: GridShape
) -> npt.NDArray[np.float64]:
    """Propagates a base Fourier coefficient vector to all grid points via rotation in reciprocal
    space.

    Args:
        coefs: Base Fourier coefficients for position ``(0,0,0)``.
        grid_shape: Shape of a unit cell of the neuron lattice.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        A four-dimensional array where the first three dimensions index the grid points, and the
        last dimension corresponds to the Fourier coefficients.

    Notes:
        By exploiting the grid structure and NumPy's vectorization this function is very efficient.
    """
    res_u, res_v, res_w = grid_shape

    center_u = get_domain() * np.array([1, 0, 0]) / np.array(grid_shape)
    rot_mat_u = get_rotation_matrix(fgrid_shape, center_u)
    rot_mat_u = csr_array(rot_mat_u)
    center_v = get_domain() * np.array([0, 1, 0]) / np.array(grid_shape)
    rot_mat_v = get_rotation_matrix(fgrid_shape, center_v)
    rot_mat_v = csr_array(rot_mat_v)
    center_w = get_domain() * np.array([0, 0, 1]) / np.array(grid_shape)
    rot_mat_w = get_rotation_matrix(fgrid_shape, center_w)
    rot_mat_w = csr_array(rot_mat_w)

    res = np.zeros((*grid_shape, rot_mat_u.shape[0]))
    res[0, 0, 0, :] = coefs.copy()

    for mw in range(1, res_w):
        res[0, 0, mw, :] = rot_mat_w.dot(res[0, 0, mw-1, :])

    for mv in range(1, res_v):
        res[0, mv, :, :] = rot_mat_v.dot(res[0, mv-1, :, :].transpose()).transpose()

    for mu in range(1, res_u):
        res[mu, :, :, :] = rot_mat_u.dot(res[mu-1, :, :, :].reshape((res_v*res_w, -1)
                                                                    ).transpose()).transpose().reshape((res_v, res_w, -1))

    return res


def get_encoders(
    grid_shape: GridShape,
    fgrid_shape: GridShape,
    cov: npt.NDArray[np.float64],
    normalize: bool = True
) -> npt.NDArray[np.float64]:
    """Computes encoders as modified Fourier coefficient vectors of three-dimensional Gaussians.

    Args:
        grid_shape: Shape of a unit cell of the neuron lattice.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.
        cov: Covariance matrix of the Gaussian.
        normalize: Whether to normalize the final encoder vectors to unit length. Defaults to True.

    Returns:
        Array with the encoder vectors as rows.
    """
    logger.info('create encoders_pose' + get_mem_info())
    gauss0_f_cropped_flat = get_0_coefs(fgrid_shape, cov)

    encoders = rotate_to_grid(gauss0_f_cropped_flat, grid_shape, fgrid_shape).reshape((np.prod(grid_shape), -1))

    final_encoders = encoders[:, encoding_mask(fgrid_shape).ravel()]

    scale_fact = 1
    if normalize:
        scale_fact = 1.0 / np.amax(np.linalg.norm(final_encoders, axis=1, keepdims=True))
        final_encoders *= scale_fact

    return final_encoders, scale_fact


# def get_eval_points(
#     grid_shape: GridShape,
#     fgrid_shape: GridShape,
#     cov: npt.NDArray[np.float64],
#     n: int = 40000
# ) -> npt.NDArray[np.float64]:
#     logger.info('create evalp_pose' + get_mem_info())
#     res_u, res_v, res_w = grid_shape

#     gauss0_f_cropped_flat = get_0_coefs(fgrid_shape, cov)

#     eval_points = np.zeros((n, np.prod(fgrid_shape)*2))
#     range_u = np.arange(res_u)
#     range_v = np.arange(res_v)
#     range_w = np.arange(res_w)

#     for i in np.arange(n):
#         mu = np.random.choice(range_u)
#         mv = np.random.choice(range_v)
#         mw = np.random.choice(range_w)

#         center = get_domain() * np.array([mu, mv, mw]) / np.array(grid_shape)
#         rot_mat = get_rotation_matrix(fgrid_shape, center)
#         coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         eval_points[i, :] = coefs_cropped_flat

#     return eval_points[:, encoding_mask(fgrid_shape).ravel()]


def shift_weights_vect_optimized(
    base_coefs_on_grid: npt.NDArray[np.float64],
    shift_vec: npt.NDArray[np.float64],
    grid_shape: GridShape,
    fgrid_shape: GridShape
) -> npt.NDArray[np.float64]:
    """Applies a constant shift vector to a set of Fourier coefficients.

    The computation is performed in reciprocal space.

    Args:
        base_coefs_on_grid: Un-shifted Fourier coefficient vectors at each grid point.
        shift_vec: Shift vector.
        grid_shape: Shape of a unit cell of the neuron lattice.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        Shifted weight matrix.
    """
    fspace_shifts = inv_fspace_base.dot(shift_vec)
    center = get_domain() * fspace_shifts
    rot_mat = get_rotation_matrix(fgrid_shape, center)
    rot_mat = csr_array(rot_mat)

    res = rot_mat.dot(base_coefs_on_grid.reshape((np.prod(grid_shape), -1)
                                                 ).transpose()).transpose().reshape((*grid_shape, -1))

    return res


def shift_weights_angle_optimized(
    base_coefs_on_grid: npt.NDArray[np.float64],
    shift: np.float64,
    grid_shape: GridShape,
    fgrid_shape: GridShape
) -> npt.NDArray[np.float64]:
    """Shifts a set of Fourier coefficients based on the preferred orientation angle as specified by
    the associated z-coordinates. Consequently, the base coefficients are shifted differently in
    each z-plane.

    The computation is performed in reciprocal space.

    Args:
        base_coefs_on_grid: Un-shifted Fourier coefficient vectors at each grid point.
        shift: Shift value indicating how far the weights should be shifted along the preferred
        direction of the individual z-planes.
        grid_shape: Shape of a unit cell of the neuron lattice.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        Transformed weight matrix.
    """
    res = np.zeros(base_coefs_on_grid.shape)

    for i in range(grid_shape[2]):
        layer_orientation_angle = i * 2 * pi / grid_shape[2]
        shift_vec = polar_to_cartesian(shift, layer_orientation_angle)
        fspace_shifts = inv_fspace_base.dot(shift_vec)
        center = get_domain() * fspace_shifts
        rot_mat = get_rotation_matrix(fgrid_shape, center)
        rot_mat = csr_array(rot_mat)

        res[:, :, i, :] = rot_mat.dot(base_coefs_on_grid[:, :, i, :].reshape(
            (grid_shape[0] * grid_shape[1], -1)).transpose()).transpose().reshape((grid_shape[0], grid_shape[1], -1))

    return res


def _get_ifft_helper(grid_shape: GridShape):
    def ifft_helper(x):
        C_rotated_tmp = unflatten_coefs(x).reshape(grid_shape)
        Z_rotated = np.fft.ifftn(C_rotated_tmp, s=grid_shape, norm='forward') / np.prod(get_domain())
        Z_rotated = np.real(Z_rotated)
        return Z_rotated
    return ifft_helper


def get_shift_con_weights(
    grid_shape: GridShape,
    tran_shift: np.float64,
    frec_con_weights: npt.NDArray[np.float64],
    rec_con_weights: npt.NDArray[np.float64]
) -> npt.NDArray[np.float64]:
    """Computes the weight matrix for the shift connection.

    Args:
        grid_shape: Shape of a unit cell of the neuron lattice.
        tran_shift: Shift value indicating how far the weights should be shifted along the preferred
        direction of the individual z-planes.
        frec_con_weights: Fourier coefficient vector of the non-transposed rec_con_weights.
        rec_con_weights: Final transposed rec_con_weights to be subtracted from the weight matrices
        to counteract the rec_con_weights when shifting.

    Returns:
        Weight matrix.
    """
    # frec_con_weights is of the non-transposed weights
    # rec_con_weights are the transposed weights
    logger.info('get shift_con_weights' + get_mem_info())
    fshift_con_weights = shift_weights_angle_optimized(frec_con_weights, tran_shift, grid_shape, grid_shape)
    shift_con_weights = np.apply_along_axis(_get_ifft_helper(grid_shape), -1, fshift_con_weights)
    shift_con_weights = shift_con_weights.reshape((np.prod(grid_shape), np.prod(grid_shape))).transpose()
    shift_con_weights = shift_con_weights - rec_con_weights

    return shift_con_weights


def get_rot_con_weights(
    grid_shape: GridShape,
    rot_shift: np.float64,
    frec_con_weights: npt.NDArray[np.float64],
    rec_con_weights: npt.NDArray[np.float64]
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Computes the weight matrices for the CW+CCW rotation connections.

    Args:
        grid_shape: Shape of a unit cell of the neuron lattice.
        rot_shift: Shift value indicating how far up/down along the z-axis the weights should be
        shifted.
        frec_con_weights: Fourier coefficient vector of the non-transposed rec_con_weights.
        rec_con_weights: Final transposed rec_con_weights to be subtracted from the weight matrices
        to counteract the rec_con_weights when rotating.

    Returns:
        CW and CCW rotation weight matrices.
    """
    # frec_con_weights is of the non-transposed weights
    # rec_con_weights are the transposed weights
    logger.info('get rot_con_weights' + get_mem_info())
    shift = np.array([0, 0, rot_shift])
    frot_con_weights_pos = shift_weights_vect_optimized(frec_con_weights, shift, grid_shape, grid_shape)
    rot_con_weights_pos = np.apply_along_axis(_get_ifft_helper(grid_shape), -1, frot_con_weights_pos)
    rot_con_weights_pos = rot_con_weights_pos.reshape(
        (np.prod(grid_shape), np.prod(grid_shape))).transpose()
    rot_con_weights_pos = rot_con_weights_pos - rec_con_weights

    frot_con_weights_neg = shift_weights_vect_optimized(frec_con_weights, -shift, grid_shape, grid_shape)
    rot_con_weights_neg = np.apply_along_axis(_get_ifft_helper(grid_shape), -1, frot_con_weights_neg)
    rot_con_weights_neg = rot_con_weights_neg.reshape(
        (np.prod(grid_shape), np.prod(grid_shape))).transpose()
    rot_con_weights_neg = rot_con_weights_neg - rec_con_weights

    return rot_con_weights_pos, rot_con_weights_neg


def get_weights_optimized(
    grid_shape: GridShape,
    weight_config: dict[np.float64]
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Computes weight matrices for the recurrent attractor connection, shift connection, and CW+CCW
    rotation connections.

    Args:
        grid_shape: Shape of a unit cell of the neuron lattice.
        weight_config: Weight shape parameters, consisting of variance and factor of the excitatory
        and inhibitory Gaussian components, and an offset.

    Returns:
        Four weight matrices.
    """
    logger.info('get weights' + get_mem_info())

    grid_shape = tuple(grid_shape)
    var_exc = weight_config['var_exc']
    var_inh = weight_config['var_inh']
    fact_exc = weight_config['fact_exc']
    fact_inh = weight_config['fact_inh']
    offset = weight_config['offset']
    tran_shift = weight_config['tran_shift']
    rot_shift = weight_config['rot_shift']

    u_diff_unwrapped, v_diff_unwrapped, w_diff_unwrapped = get_3d_distances_unwrapped(grid_shape)
    pos_unwrapped = np.stack((u_diff_unwrapped[0], v_diff_unwrapped[0], w_diff_unwrapped[0]), axis=-1)

    Z_computed = mex_hat(pos_unwrapped, var_exc, var_inh, fact_exc, fact_inh, offset).reshape(grid_shape)

    C_computed = np.fft.fftn(Z_computed, s=grid_shape, norm='forward') * np.prod(get_domain())
    C_computed = flatten_coefs(C_computed)

    logger.info('get rec_con_weights' + get_mem_info())
    frec_con_weights = rotate_to_grid(C_computed, grid_shape, grid_shape)
    rec_con_weights = np.apply_along_axis(_get_ifft_helper(grid_shape), -1, frec_con_weights)
    rec_con_weights = rec_con_weights.reshape((np.prod(grid_shape), np.prod(grid_shape))).transpose()

    shift_con_weights = get_shift_con_weights(grid_shape, tran_shift, frec_con_weights, rec_con_weights)

    rot_con_weights_pos, rot_con_weights_neg = get_rot_con_weights(
        grid_shape, rot_shift, frec_con_weights, rec_con_weights)

    return rec_con_weights, shift_con_weights, rot_con_weights_pos, rot_con_weights_neg


def get_attractor_network(
    ens_cfg: nengo.Config,
    tau: np.float64,
    rec_con_weights: npt.NDArray[np.float64] = None,
    **kwargs
):
    """Creates a Nengo ensemble and recurrent connection to obtain attractor dynamics.

    Args:
        ens_cfg: Parameters for the ensemble, including encoders.
        tau: Synaptic time constant.
        rec_con_weights: Recurrent connection weights. May be sparse. If not specified, the weights
        are computed by Nengo based on the encoders. Defaults to None.
        **kwargs: Parameters for the wrapper network, e.g. label or seed.

    Returns:
        A Nengo network containing the recurrently connected attractor ensemble.

    Notes:
        Specifies the block_shape config parameter for splitting the ensemble onto Loihi cores.
    """
    n_neurons = ens_cfg[nengo.Ensemble].encoders.shape[0]
    dimensions = ens_cfg[nengo.Ensemble].encoders.shape[1]

    with nengo.Network(**kwargs) as net, ens_cfg:
        nengo_loihi.add_params(net)
        net.attractor_ens = nengo.Ensemble(n_neurons,
                                           dimensions,
                                           label='attractor_network')
        # interpret the ensemble as a three-dimensional grid and split into 4*4*4 blocks
        net.config[net.attractor_ens].block_shape = nengo_loihi.BlockShape((4, 4, 4), (12, 12, 12))

        # constant global inhibition
        # net.global_inhib_node = nengo.Node(getf_global_inhib(dt))
        # ginh = np.ones((dim_pose,1))*-10
        # ginh[0,0] = -1
        # nengo.Connection(net.global_inhib_node, net.pose, transform=ginh, synapse=tau)
        # nengo.Connection(net.global_inhib_node, net.pose.neurons, transform=[[-1.0]] * net.pose.n_neurons, synapse=None)

        # recurrent connection of the attractor network
        if rec_con_weights is None:
            net.rec_con = nengo.Connection(
                net.attractor_ens,
                net.attractor_ens,
                # function=lambda x: x/tau,
                # function=lambda x: x * 0.5,  # leaky integrator
                solver=nengo.solvers.LstsqL2(weights=True),
                synapse=tau,
                label='attractor_dynamics')
        else:
            net.rec_con = nengo.Connection(
                net.attractor_ens.neurons,
                net.attractor_ens.neurons,
                # transform=rec_con_weights,
                transform=nengo.Sparse(rec_con_weights.shape, init=rec_con_weights),
                synapse=tau,
                label='attractor_dynamics')

    return net


def _get_rotate_feedback_function(fgrid_shape, shift):
    def rotate_feedback_function(x):
        rot_mat = get_rotation_matrix(fgrid_shape, shift)
        mask_flat = np.invert(encoding_mask(fgrid_shape).ravel())
        rot_mat = np.delete(rot_mat, mask_flat, axis=0)
        rot_mat = np.delete(rot_mat, mask_flat, axis=1)

        out = rot_mat.dot(x)

        return out

    return rotate_feedback_function


tangential_velocity_max = 1
angular_velocity_max = 1


def get_pose_network(
    grid_shape: GridShape,
    fgrid_shape: GridShape,
    cov: npt.NDArray[np.float64],
    tau: np.float64,
    dt: np.float64,
    rec_con_weights: npt.NDArray[np.float64] = None,
    shift_con_weights: npt.NDArray[np.float64] = None,
    rot_con_weights_pos: npt.NDArray[np.float64] = None,
    rot_con_weights_neg: npt.NDArray[np.float64] = None,
    _config=None,
    **kwargs
):
    """Creates a Nengo network capable of performing path integration.

    Multiple pose (position+orientation) estimates can be sustained simultaneously. Persistent reset
    input can inhibit any other existing bumps and establish a single new bump at a desired
    position.

    Args:
        grid_shape: Shape of a unit cell of the neuron lattice.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.
        cov: Covariance matrix of the Gaussian bumps.
        tau: Synaptic time constant.
        dt: Simulation time step in seconds.
        rec_con_weights: Recurrent connection weights for the attractor ensemble. May be sparse. If
        not specified, the weights are computed by Nengo based on the encoders. Defaults to None.
        shift_con_weights: Connection weights for translation. May be sparse. If not specified, the
        translation module is omitted. Defaults to None.
        rot_con_weights_pos: Connection weights for CCW rotation. May be sparse. If not specified,
        the CCW rotation module is omitted. Defaults to None.
        rot_con_weights_neg: Connection weights for CW rotation. May be sparse. If not specified,
        the CW rotation module is omitted. Defaults to None.

    Returns:
        A Nengo network containing the desired components for an attractor network, potentially
        capable of performing path integration (depending on the parameters).
    """
    timesteps_per_sec = round(1/dt)
    with nengo.Network(**kwargs) as net:
        nengo_loihi.add_params(net)
        dim_pose = encoding_len(fgrid_shape)
        n_neurons = np.prod(np.array(grid_shape))

        num_inputs = n_neurons + 2  # tangential + angular (latter can be negative)
        net.input = nengo.Node(size_in=num_inputs, label='input')
        # make the node non-passthrough to allow for functions on outgoing connections
        net.input.output = lambda t, x: x

        encoders_pose, scale_fact_pose = get_encoders(grid_shape, fgrid_shape, cov)
        # encoders_pose = csr_array(encoders_pose)

        # evalp_pose = get_eval_points(grid_shape, fgrid_shape, cov, n=n_eval_points)
        # evalp_pose *= scale_fact_pose
        # # include grid positions as eval_points
        # evalp_pose = np.concatenate((encoders_pose, evalp_pose), axis=0)
        # # evalp_pose = csr_array(evalp_pose)

        ens_cfg = nengo.Config(nengo.Ensemble)
        ens_cfg[nengo.Ensemble].encoders = encoders_pose
        ens_cfg[nengo.Ensemble].eval_points = encoders_pose
        # ens_cfg[nengo.Ensemble].intercepts = nengo.dists.Choice([0.0])  # e.g. 0.0325 corresponds to slight constant inhibition
        # ens_cfg[nengo.Ensemble].max_rates = nengo.dists.Choice([120])  # recommended for Loihi is 100-120
        ens_cfg[nengo.Ensemble].gain = nengo.dists.Choice([2.68423963])
        ens_cfg[nengo.Ensemble].bias = nengo.dists.Choice([_config['bias']])  # 1 by default -> constant inhibition
        ens_cfg[nengo.Ensemble].normalize_encoders = False
        # ens_cfg[nengo.Ensemble].neuron_type = FastLIF()
        # intercepts=nengo.dists.Exponential(0.15, 0.0, 1.0))
        # neuron_type=nengo.RectifiedLinear()
        if _config['enable_noise']:
            noise = nengo.processes.WhiteNoise(nengo.dists.Gaussian(mean=0, std=_config['noise_std']), default_size_out=1)
            ens_cfg[nengo.Ensemble].noise = noise

        inhib_input_ens_cfg = nengo.Config(nengo.Ensemble)
        inhib_input_ens_cfg[nengo.Ensemble].encoders = [[1]]
        inhib_input_ens_cfg[nengo.Ensemble].intercepts = nengo.dists.Uniform(0, 0)
        inhib_input_ens_cfg[nengo.Ensemble].max_rates = nengo.dists.Uniform(timesteps_per_sec, timesteps_per_sec)
        inhib_input_ens_cfg[nengo.Ensemble].neuron_type = nengo.SpikingRectifiedLinear()

        net.attractor_network = get_attractor_network(
            ens_cfg,
            tau,
            rec_con_weights=rec_con_weights,
            label='attractor_network',
            seed=kwargs.setdefault('seed', 0))

        # get same results as with lowering the bias
        # tmpy = nengo.Node(-0.03/2.68423963)
        # nengo.Connection(tmpy, net.attractor_network.attractor_ens.neurons, transform=np.ones((n_neurons, 1)), synapse=None)

        net.init_attractor = nengo.Connection(
            net.input[:n_neurons],
            net.attractor_network.attractor_ens.neurons,
            transform=tau,
            synapse=tau,
            label='init_attractor')

        # net.global_inhib = nengo.Node(0.15)
        # nengo.Connection(
        #     net.global_inhib,
        #     net.attractor_network.attractor_ens.neurons,
        #     transform=[[-1./14.5]] * n_neurons)

        net.output = nengo.Node(size_in=n_neurons, label='readout_probe')
        # net.output1 = nengo.Node(size_in=dim_pose//2, label='readout_probe1')
        # net.output2 = nengo.Node(size_in=dim_pose//2, label='readout_probe2')

        # gauss0_f_cropped_flat = get_0_coefs(fgrid_shape, cov)
        # fact = gauss0_f_cropped_flat[0] / gauss0_f_cropped_flat[2]

        net.readout = nengo.Connection(
            net.attractor_network.attractor_ens.neurons,
            net.output,
            # function=getf_decode_pose(fgrid_shape, scale_fact_pose, fact),
            synapse=0.01,  # TODO: tune further?
            label='readout')
        # net.readout = nengo.Connection(
        #     net.attractor_network.attractor_ens[:(dim_pose//2)],
        #     net.output1,
        #     # function=getf_decode_pose(fgrid_shape, scale_fact_pose, fact),
        #     synapse=0.01,
        #     label='readout1')
        # net.readout = nengo.Connection(
        #     net.attractor_network.attractor_ens[(dim_pose//2):],
        #     net.output2,
        #     # function=getf_decode_pose(fgrid_shape, scale_fact_pose, fact),
        #     synapse=0.01,
        #     label='readout2')

        # translation module
        if shift_con_weights is not None:
            with ens_cfg:
                net.shift_ens = nengo.Ensemble(
                    n_neurons=n_neurons,
                    dimensions=dim_pose,
                    label='attractor_for_translation')
                net.config[net.shift_ens].block_shape = nengo_loihi.BlockShape((4, 4, 4), (12, 12, 12))

            if _config['continuous_inhib']:
                net.shift_inhib = nengo.Connection(
                    net.input[n_neurons+0:n_neurons+2],
                    net.shift_ens.neurons,
                    function=lambda x: pose.input.vel_to_shift_inhib(x[0], x[1]),  # convert velocity to inhibition
                    transform=[[-1]] * n_neurons,
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='shift_inhib')
            else:
                # a seed here determines the initial state of the ensemble
                with inhib_input_ens_cfg:
                    net.shift_inhib_input_ens = nengo.Ensemble(
                        n_neurons=1,
                        dimensions=1,
                        label='shift_inhib_input_ens')

                net.shift_inhib_input = nengo.Connection(
                    net.input[n_neurons+0],
                    net.shift_inhib_input_ens,
                    function=lambda x: 1.0 - (max(0.0, x)/tangential_velocity_max),  # convert velocity to inhibition
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='shift_inhib_input')

                net.shift_inhib = nengo.Connection(
                    net.shift_inhib_input_ens.neurons,
                    net.shift_ens.neurons,
                    transform=[[-dt]] * n_neurons,
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='shift_inhib')

            # nengo.Connection(
            #     net.global_inhib,
            #     net.shift_ens.neurons,
            #     transform=[[-1./14.5]] * n_neurons)

            # TODO: synapse? tau/2?
            # net.shift_con = nengo.Connection(
            #     net.attractor_network.attractor_ens,
            #     net.shift_ens,
            #     solver=nengo.solvers.LstsqL2(weights=True),
            #     # transform=nengo.Sparse(rec_con_weights.shape, init=rec_con_weights),
            #     # transform=np.eye(num_neurons_pose),
            #     # transform=nengo.Sparse((num_neurons_pose, num_neurons_pose), init=identity(num_neurons_pose, format='csr')),
            #     label='init_attractor_for_translation')
            if _config['full_init_con']:
                net.shift_init_con = nengo.Connection(
                    net.attractor_network.attractor_ens.neurons,
                    net.shift_ens.neurons,
                    transform=nengo.Sparse(rec_con_weights.shape, init=rec_con_weights),
                    # Default synapse  # synapse=tau,
                    label='shift_init_con')
            else:
                net.shift_init_con = nengo.Connection(
                    net.attractor_network.attractor_ens.neurons,
                    net.shift_ens.neurons,
                    transform=nengo.Sparse((n_neurons, n_neurons), init=identity(n_neurons) * dt),
                    # Default synapse  # synapse=tau,
                    label='shift_init_con')

            # eval_points_extended = np.zeros((*grid_shape, full_dim))
            # ep_tmp = np.zeros((*grid_shape, full_dim))
            # ep_tmp[:, :, :, encoding_mask(fgrid_shape).ravel()] = evalp_pose.reshape((*grid_shape, -1))
            # for i in range(grid_shape[2]):
            #     layer_orientation_angle = i * 2 * pi / grid_shape[2]
            #     shift_vec = polar_to_cartesian(0.25*1/8, layer_orientation_angle)
            #     fspace_shifts = inv_fspace_base.dot(shift_vec)
            #     center = get_domain() * fspace_shifts
            #     rot_mat = _rot_mat_complete(grid_shape, center)
            #     rot_mat = csr_array(rot_mat)

            #     eval_points_extended[:, :, i, :] = rot_mat.dot(ep_tmp[:, :, i, :].reshape(
            #         (grid_shape[0] * grid_shape[1], -1)).transpose()).transpose().reshape((grid_shape[0], grid_shape[1], -1))

            # eval_point_targets = eval_points_extended.reshape((np.prod(grid_shape), -1))[:, encoding_mask(fgrid_shape).ravel()]

            # encoders_pose6_tmp = get_encoders_optimized(grid_shape, fgrid_shape, cov).reshape((*grid_shape, -1))
            # encoders_pose6_tmp = encoders_pose6_tmp / np.amax(np.linalg.norm(encoders_pose6_tmp, axis=-1))
            # encoders_pose6 = np.zeros((*grid_shape, np.prod(fgrid_shape)*2))
            # encoders_pose6[:, :, :, encoding_mask(fgrid_shape).ravel()] = encoders_pose6_tmp
            # ep_tmp6 = np.zeros_like(encoders_pose6)
            # for i in range(grid_shape[2]):
            #     layer_orientation_angle = i * 2 * pi / grid_shape[2]
            #     shift_vec = polar_to_cartesian(0.25*1/8, layer_orientation_angle)
            #     fspace_shifts = inv_fspace_base.dot(np.array([1/8,3/8*get_domain()[1],5/8]))  # worked
            #     center = get_domain() * fspace_shifts
            #     rot_mat = pose.freq_space._rot_mat_complete(grid_shape, center)
            #     rot_mat = csr_array(rot_mat)

            #     ep_tmp6[:, :, i, :] = rot_mat.dot(encoders_pose6[:, :, i, :].reshape(
            #         (grid_shape[0] * grid_shape[1], -1)).transpose()).transpose().reshape((grid_shape[0], grid_shape[1], -1))

            # eval_point_targets = ep_tmp6.reshape((np.prod(grid_shape), -1))[:, encoding_mask(fgrid_shape).ravel()]

            net.shift_con = nengo.Connection(
                net.shift_ens.neurons,
                net.attractor_network.attractor_ens.neurons,
                # transform=shift_con_weights,
                transform=nengo.Sparse(shift_con_weights.shape, init=shift_con_weights),
                synapse=tau,  # TODO: tau/2?
                label='shift_con')
            # full_dim = np.prod(fgrid_shape)*2
            # eval_points_extended = np.zeros((*grid_shape, full_dim))
            # eval_points_extended[:, :, :, encoding_mask(fgrid_shape).ravel()] = evalp_pose.reshape((*grid_shape, -1))
            # eval_point_targets = shift_weights_angle_optimized(eval_points_extended, 0.35*1/grid_shape[2], grid_shape, fgrid_shape)[:, :, :, encoding_mask(fgrid_shape).ravel()].reshape((np.prod(grid_shape), -1))
            # net.shift_feedback_con = nengo.Connection(
            #     net.shift_ens,
            #     net.attractor_network.attractor_ens,
            #     solver=nengo.solvers.LstsqL2(weights=True),
            #     eval_points=evalp_pose,  # encoders_pose6_tmp.reshape((np.prod(fgrid_shape), -1)),
            #     function=eval_point_targets,
            #     synapse=tau,
            #     label='translate_fwd')

        # CCW rotation module
        if rot_con_weights_pos is not None:
            with ens_cfg:
                net.ccw_rot_ens = nengo.Ensemble(
                    n_neurons=n_neurons,
                    dimensions=dim_pose,
                    label='ccw_rot_ens')
                net.config[net.ccw_rot_ens].block_shape = nengo_loihi.BlockShape((4, 4, 4), (12, 12, 12))

            # nengo.Connection(
            #     net.input[dim_pose+1],
            #     net.ccw_rot_ens.neurons,
            #     function=lambda x: 1.0 - (max(0.0, x)/angular_velocity_max),  # convert velocity to inhibition
            #     transform=[[-1]] * n_neurons,
            #     synapse=None,
            #     label='inhibit_ccw_rotation')

            if _config['continuous_inhib']:
                net.ccw_rot_inhib = nengo.Connection(
                    net.input[n_neurons+0:n_neurons+2],
                    net.ccw_rot_ens.neurons,
                    function=lambda x: pose.input.vel_to_ccw_inhib(x[0], x[1]),  # convert velocity to inhibition
                    transform=[[-1]] * n_neurons,
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='ccw_rot_inhib')
            else:
                with inhib_input_ens_cfg:
                    net.ccw_rot_inhib_input_ens = nengo.Ensemble(
                        n_neurons=1,
                        dimensions=1,
                        label='ccw_rot_inhib_input_ens')

                net.ccw_rot_inhib_input = nengo.Connection(
                    net.input[n_neurons+1],
                    net.ccw_rot_inhib_input_ens,
                    function=lambda x: 1.0 - (max(0.0, x)/angular_velocity_max),  # convert velocity to inhibition
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='ccw_rot_inhib_input')

                net.ccw_rot_inhib = nengo.Connection(
                    net.ccw_rot_inhib_input_ens.neurons,
                    net.ccw_rot_ens.neurons,
                    transform=[[-dt]] * n_neurons,
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='ccw_rot_inhib')

            # nengo.Connection(
            #     net.global_inhib,
            #     net.ccw_rot_ens.neurons,
            #     transform=[[-1./14.5]] * n_neurons)

            # TODO: synapse? tau/2?
            # net.rotate_con_pos = nengo.Connection(
            #     net.attractor_network.attractor_ens,
            #     net.ccw_rot_ens,
            #     solver=nengo.solvers.LstsqL2(weights=True),
            #     # transform=nengo.Sparse(rec_con_weights.shape, init=rec_con_weights),
            #     # transform=nengo.Sparse((num_neurons_pose, num_neurons_pose), init=identity(num_neurons_pose, format='csr')),
            #     label='init_attractor_for_ccw_rotation')
            if _config['full_init_con']:
                net.ccw_rot_init_con = nengo.Connection(
                    net.attractor_network.attractor_ens.neurons,
                    net.ccw_rot_ens.neurons,
                    transform=nengo.Sparse(rec_con_weights.shape, init=rec_con_weights),
                    # Default synapse  # synapse=tau,
                    label='ccw_rot_init_con')
            else:
                net.ccw_rot_init_con = nengo.Connection(
                    net.attractor_network.attractor_ens.neurons,
                    net.ccw_rot_ens.neurons,
                    transform=nengo.Sparse((n_neurons, n_neurons), init=identity(n_neurons) * dt),
                    # Default synapse  # synapse=tau,
                    label='ccw_rot_init_con')

            # eval_points_extended = np.zeros((np.prod(grid_shape), full_dim))
            # eval_points_extended[:, encoding_mask(fgrid_shape).ravel()] = evalp_pose
            # rot_mat = _rot_mat_complete(fgrid_shape, get_domain() * inv_fspace_base.dot(np.array([0,0.25*1/8,0])))
            # eval_point_targets = rot_mat.dot(eval_points_extended.transpose()).transpose()[:, encoding_mask(fgrid_shape).ravel()]

            net.ccw_rot_con = nengo.Connection(
                net.ccw_rot_ens.neurons,
                net.attractor_network.attractor_ens.neurons,
                # transform=rot_con_weights_pos,
                transform=nengo.Sparse(rot_con_weights_pos.shape, init=rot_con_weights_pos),
                synapse=tau,  # TODO: tau/2?
                label='ccw_rot_con')
            # net.rotate_feedback_con_pos = nengo.Connection(
            #     net.ccw_rot_ens,
            #     net.attractor_network.attractor_ens,
            #     solver=nengo.solvers.LstsqL2(weights=True),
            #     function=_get_rotate_feedback_function(fgrid_shape, np.array([0, 0, 0.35*1/grid_shape[2]])),
            #     # eval_points=evalp_pose,
            #     # function=eval_point_targets,
            #     synapse=tau,
            #     label='rotate_ccw')

        # CW rotation module
        if rot_con_weights_neg is not None:
            with ens_cfg:
                net.cw_rot_ens = nengo.Ensemble(
                    n_neurons=n_neurons,
                    dimensions=dim_pose,
                    label='cw_rot_ens')
                net.config[net.cw_rot_ens].block_shape = nengo_loihi.BlockShape((4, 4, 4), (12, 12, 12))

            # nengo.Connection(
            #     net.input[dim_pose+1],
            #     net.cw_rot_ens.neurons,
            #     function=lambda x: 1.0 + (min(0.0, x)/angular_velocity_max),  # convert velocity to inhibition
            #     transform=[[-1]] * n_neurons,
            #     synapse=None,
            #     label='inhibit_cw_rotation')

            if _config['continuous_inhib']:
                net.cw_rot_inhib = nengo.Connection(
                    net.input[n_neurons+0:n_neurons+2],
                    net.cw_rot_ens.neurons,
                    function=lambda x: pose.input.vel_to_cw_inhib(x[0], x[1]),  # convert velocity to inhibition
                    transform=[[-1]] * n_neurons,
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='cw_rot_inhib')
            else:
                with inhib_input_ens_cfg:
                    net.cw_rot_inhib_input_ens = nengo.Ensemble(
                        n_neurons=1,
                        dimensions=1,
                        label='cw_rot_inhib_input_ens')

                net.cw_rot_inhib_input = nengo.Connection(
                    net.input[n_neurons+1],
                    net.cw_rot_inhib_input_ens,
                    function=lambda x: 1.0 + (min(0.0, x)/angular_velocity_max),  # convert velocity to inhibition
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='cw_rot_inhib_input')

                net.cw_rot_inhib = nengo.Connection(
                    net.cw_rot_inhib_input_ens.neurons,
                    net.cw_rot_ens.neurons,
                    transform=[[-dt]] * n_neurons,
                    # Default synapse  # synapse=tau,
                    synapse=None,
                    label='cw_rot_inhib')

            # nengo.Connection(
            #     net.global_inhib,
            #     net.cw_rot_ens.neurons,
            #     transform=[[-1./14.5]] * n_neurons)

            # TODO: synapse? tau/2?
            # net.rotate_con_neg = nengo.Connection(
            #     net.attractor_network.attractor_ens,
            #     net.cw_rot_ens,
            #     solver=nengo.solvers.LstsqL2(weights=True),
            #     # transform=nengo.Sparse(rec_con_weights.shape, init=rec_con_weights),
            #     # transform=nengo.Sparse((num_neurons_pose, num_neurons_pose), init=identity(num_neurons_pose, format='csr')),
            #     label='init_attractor_for_cw_rotation')
            if _config['full_init_con']:
                net.cw_rot_init_con = nengo.Connection(
                    net.attractor_network.attractor_ens.neurons,
                    net.cw_rot_ens.neurons,
                    transform=nengo.Sparse(rec_con_weights.shape, init=rec_con_weights),
                    # Default synapse  # synapse=tau,
                    label='cw_rot_init_con')
            else:
                net.cw_rot_init_con = nengo.Connection(
                    net.attractor_network.attractor_ens.neurons,
                    net.cw_rot_ens.neurons,
                    transform=nengo.Sparse((n_neurons, n_neurons), init=identity(n_neurons) * dt),
                    # Default synapse  # synapse=tau,
                    label='cw_rot_init_con')

            net.cw_rot_con = nengo.Connection(
                net.cw_rot_ens.neurons,
                net.attractor_network.attractor_ens.neurons,
                # transform=rot_con_weights_neg,
                transform=nengo.Sparse(rot_con_weights_neg.shape, init=rot_con_weights_neg),
                synapse=tau,  # TODO: tau/2?
                label='cw_rot_con')
            # net.rotate_feedback_con_neg = nengo.Connection(
            #     net.cw_rot_ens,
            #     net.attractor_network.attractor_ens,
            #     solver=nengo.solvers.LstsqL2(weights=True),
            #     function=_get_rotate_feedback_function(fgrid_shape, np.array([0, 0, -0.35*1/grid_shape[2]])),
            #     synapse=tau,
            #     label='rotate_cw')

    return net
