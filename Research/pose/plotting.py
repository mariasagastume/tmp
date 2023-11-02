"""
Generate static and interactive plots of various aspects of the project during development, for evaluation, or for the documentation.

Note:
    Not part of the public API.
"""
# __all__ = []  # optionally uncomment for generating docs
# import ipywidgets as widgets
import logging
from math import ceil, pi, sqrt
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.ticker import ScalarFormatter
import numpy as np
import pathlib

from pose.experiments import get_time_array
from pose.hex import (
    fspace_base,
    get_3d_coordinates_unwrapped_vectorized
)
from pose.io_utils import get_pose_lib_path
from pose.nengo_utils import mex_hat


logger = logging.getLogger(__name__)


# global config
fe = mpl.font_manager.FontEntry(
    fname=get_pose_lib_path() / 'fonts' / 'gnu_freefont' / 'FreeSans.otf',
    name='GNU FreeSans'
)
mpl.font_manager.fontManager.ttflist.insert(0, fe)
# mpl.rcParams['font.family'] = fe.name
# mpl.rcParams['font.family'] = 'Arial'

file_dir = pathlib.Path(__file__).parent
mpl.style.use(file_dir / 'regular.mplstyle')


_mm = 1/25.4
_text_width = 170  # mm
_text_height = 247  # mm
_column_width = 82.5  # mm
_3column_width = 160.0/3.0  # mm
_4column_width = 155.0/4.0  # mm
_page_width = 210  # mm
_page_height = 297  # mm
_text_width_in = _text_width * _mm  # inch
_text_height_in = _text_height * _mm  # inch
_column_width_in = _column_width * _mm  # inch
_3column_width_in = _3column_width * _mm  # inch
_4column_width_in = _4column_width * _mm  # inch
_page_width_in = _page_width * _mm  # inch
_page_height_in = _page_height * _mm  # inch


def plot_multi(u, v, w, data1, th, cmap='coolwarm', show_plots=False):
    """Generate a summary plot for the specified attractor state.

    It contains a three-dimensional plot and projections along the x- and y-axis.
    """

    g_to_plot = data1

    # plt.rcParams['figure.dpi'] = 300

    fig = plt.figure()
    ax = fig.add_subplot(131, projection='3d')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    c = g_to_plot.flatten()
    ind = c > th
    c = c[ind]

    x = u.flatten()[ind]
    y = v.flatten()[ind]
    z = w.flatten()[ind]

    ax.scatter(x, y, z, c=c, cmap=cmap)

    fig.tight_layout(pad=5.0)

    # project along the x-axis
    xflat = np.amax(g_to_plot, axis=0)

    proj_x = fig.add_subplot(132)
    proj_x.set_title('project x')
    proj_x.contourf(v[0, :, :], w[0, :, :], xflat, cmap=cmap)
    proj_x.set_xlabel('y')
    proj_x.set_ylabel('z')
    proj_x.set_xlim([-1, 1])
    proj_x.set_ylim([-1, 1])
    # proj_x.axis('equal')
    proj_x.set_aspect('equal', 'box')
    proj_x.grid(which='major', linestyle=':', linewidth='0.7', color='black')
    proj_x.minorticks_on()
    proj_x.grid(which='minor', linestyle=':', linewidth='0.3', color='black')

    # project along the y-axis
    yflat = np.amax(g_to_plot, axis=1)

    proj_y = fig.add_subplot(133)
    proj_y.set_title('project y')
    proj_y.contourf(u[:, 0, :], w[:, 0, :], yflat, cmap=cmap)
    proj_y.set_xlabel('x')
    proj_y.set_ylabel('z')
    proj_y.set_xlim([-1, 1])
    proj_y.set_ylim([-1, 1])
    proj_y.set_aspect('equal', 'box')
    proj_y.grid(which='major', linestyle=':', linewidth='0.7', color='black')
    proj_y.minorticks_on()
    proj_y.grid(which='minor', linestyle=':', linewidth='0.3', color='black')

    if show_plots:
        plt.show()

    return (fig, (ax, proj_x, proj_y))


def plot_gauss_evo(u, v, w, data1, th_fact=0.9, time_points=[], show_plots=False):
    """Generate summary plots of the attractor state for the specified time points."""

    Nu = u.shape[0]
    Nv = v.shape[1]
    Nw = w.shape[2]
    plots = []
    for t in time_points:
        if show_plots:
            print('t=', t)
        max_val = np.max(data1[t, :])
        plots.append(plot_multi(u, v, w, data1[t, :].reshape(
            (Nu, Nv, Nw)), th=max_val*th_fact, show_plots=show_plots)[0])
    return plots


def plot_sim(time, data, s=1, cmap='coolwarm'):
    """Generate a summary plot for the specified attractor state.

    It contains a three-dimensional plot and projections along the x-, y-, and z-axis.
    """

    # plt.rcParams['figure.dpi'] = 300

    timeseq = np.arange(data.shape[0])

    # fig, axs = plt.subplots(1, figsize = (12,4))
    # axs.plot(time[:], data[:,:])
    # axs.set_title("Pose estimate")
    # axs.set_xlabel("time[s]")
    # axs.legend(['x','y','theta'])
    # axs.set_ylim([-2, 2])

    fig = plt.figure()
    fig.set_figheight(12)
    fig.set_figwidth(12)
    fig.tight_layout()

    proj_x = fig.add_subplot(221)
    proj_x.set_title('project x (right)')
    # proj_x.plot(*data[:,1:].T)
    proj_x.scatter(*data[:, 1:].T, s=s, c=timeseq, cmap=cmap)
    proj_x.set_xlabel('y')
    proj_x.set_ylabel('z')
    proj_x.set_xlim([-1, 1])
    proj_x.set_ylim([-1, 1])
    # proj_x.axis('equal')
    proj_x.set_aspect('equal', 'box')

    ax = fig.add_subplot(222, projection='3d')
    # ax.plot(*data.T)
    tmp = ax.scatter3D(*data.T, s=s, c=timeseq, cmap=cmap)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    proj_y = fig.add_subplot(223)
    proj_y.set_title('project y (front)')
    # proj_y.plot(*data[:,[0,2]].T)
    proj_y.scatter(*data[:, [0, 2]].T, s=s, c=timeseq, cmap=cmap)
    proj_y.set_xlabel('x')
    proj_y.set_ylabel('z')
    proj_y.set_xlim([-1, 1])
    proj_y.set_ylim([-1, 1])
    proj_y.set_aspect('equal', 'box')

    proj_z = fig.add_subplot(224)
    proj_z.set_title('project z (top)')
    # proj_z.plot(*data[:,:-1].T)
    proj_z.scatter(*data[:, :-1].T, s=s, c=timeseq, cmap=cmap)
    proj_z.set_xlabel('x')
    proj_z.set_ylabel('y')
    proj_z.set_xlim([-1, 1])
    proj_z.set_ylim([-1, 1])
    proj_z.set_aspect('equal', 'box')

    fig.colorbar(tmp, ax=ax, orientation='horizontal')

    return fig


def plot_pose_estimate_timeseries(trange, naive_estimates, multiscale_estimate, sample_every, ax, xlim, ylim, ylabel=''):
    num_levels = naive_estimates.shape[0]

    # plt.rcParams['figure.dpi'] = 300
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xlabel('time ['+str(sample_every)+'s]')
    ax.set_ylabel(ylabel + ' [au]')
    # ax.grid(axis='y', which='major', linestyle=':', linewidth='0.7', color='black')
    ax.minorticks_on()
    ax.grid(axis='y', which='minor', linewidth='0.3')
    # ax.plot(trange, multiscale_estimate, 'o', markersize=3, label="mscale est.")

    for i in range(num_levels):
        ax.plot(trange, conversion_helper(
            naive_estimates[i, :]), 'o', markersize=3, label='level '+str(i)+' [unscaled]')

    # plt.plot(np.arange(num_timepoints), summed_levels/num_levels, label="sum_eq")
    # plt.plot(np.arange(num_timepoints), summed_weighted_levels/num_levels, label="sum")
    ax.legend(loc="upper right")
    # ax.legend(loc="upper right", frameon=True, fancybox=True, framealpha=0.5)


def plot_velocity_repr_timeseries(velocity_repr, sample_every, ax, ylabel=''):
    num_levels = velocity_repr.shape[0]
    num_timepoints = velocity_repr.shape[1]

    ax.set_xlim([0, num_timepoints])
    ax.set_ylim([-1.2, 1.2])
    ax.set_xlabel('time ['+str(sample_every)+'s]')
    ax.set_ylabel(ylabel)

    for i in range(num_levels):
        ax.plot(np.arange(num_timepoints), velocity_repr[i, :], label='level '+str(i))

    # ax.grid(axis='y', which='major', linestyle=':', linewidth='0.7', color='black')
    # ax.minorticks_on()
    # ax.grid(axis='y', which='minor', linewidth='0.3')


def scatter(ax, x, y, z, color, alpha_arr, **kwarg):
    r, g, b, _ = mpl.colors.to_rgba(color)
    color = [(r, g, b, alpha) for alpha in alpha_arr]
    ax.scatter(x, y, z, c=color, **kwarg)


def plot_stuff(value_arr, coords_on_R_arr):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # ax.set_xlim3d(-0.51, 0.51)
    # ax.set_ylim3d(-0.51, 0.51)
    # ax.set_zlim3d(-0.51, 0.51)

    sc = ax.scatter(coords_on_R_arr[:, 0], coords_on_R_arr[:, 1], coords_on_R_arr[:, 2], c=value_arr, cmap='viridis_r', depthshade=False)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    fig.colorbar(sc, ax=ax)

    plt.show()


def plot_stuff_alpha(value_arr, coords_on_R_arr):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    scatter(ax, coords_on_R_arr[:, 0], coords_on_R_arr[:, 1], coords_on_R_arr[:, 2], color='red', alpha_arr=value_arr, depthshade=False)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def plot_parallelogram(ax, offset=[0, 0], **kwargs):
    x = [0+offset[0], 1+offset[0], 1.5+offset[0], 0.5+offset[0]]
    y = [0+offset[1], 0+offset[1], sqrt(3)/2+offset[1], sqrt(3)/2+offset[1]]
    kwargs.setdefault('fill', False)
    ax.add_patch(mpl.patches.Polygon(xy=list(zip(x, y)), **kwargs))


def plot_hexagon(ax, offset=[0, 0], **kwargs):
    x = [0+offset[0], 0.5+offset[0], 0.5+offset[0], 0+offset[0], -0.5+offset[0], -0.5+offset[0]]
    y = [-1/sqrt(3)+offset[1], -1/(2*sqrt(3))+offset[1], 1/(2*sqrt(3))+offset[1], 1/sqrt(3)+offset[1], 1/(2*sqrt(3))+offset[1], -1/(2*sqrt(3))+offset[1]]
    ax.add_patch(mpl.patches.Polygon(xy=list(zip(x, y)), fill=False, **kwargs))


def plot_square(ax):
    x = [0, sqrt(3)/2, sqrt(3)/2, 0]
    y = [0, 0, 1, 1]
    ax.add_patch(mpl.patches.Polygon(xy=list(zip(x, y)), fill=False))


def plot_square2(ax):
    x = [0, 1, 1, 0]
    y = [0, 0, 1, 1]
    ax.add_patch(mpl.patches.Polygon(xy=list(zip(x, y)), fill=False))


def plot_hex_grid(ax, XX, YY, **kwargs):
    kwargs.setdefault('facecolor', 'lightgrey')
    # kwargs.setdefault('s', 2)
    ax.scatter(XX, YY, **kwargs)


def update_interactive_plot_wrapper(fig, axes, XXX, YYY, ZZZ, XX_zproj, YY_zproj, YY_xproj, ZZ_xproj, data, bump_centers, sample_every, trange_offset, t=0):
    update_interactive_plot(fig, axes[0], data[0], bump_centers, XX_zproj, YY_zproj, sample_every, trange_offset, t=t)
    update_interactive_plot_xproj(fig, axes[1], data[1], bump_centers, YY_xproj, ZZ_xproj, sample_every, trange_offset, t=t)
    update_interactive_plot_3d(fig, axes[2], data[2], bump_centers, XXX, YYY, ZZZ, sample_every, trange_offset, t=t)

    fig.canvas.draw()


def update_interactive_plot(fig, ax, data, bump_centers, X, Y, sample_every, trange_offset, t=0):
    """Provides an interactive plot of the time evolution of the activity
    packet. Expects the data as ndarray of shape
    (timepoints, np.prod(resolution_shape)).
    """
    """Remove old contours from plot and plot new one."""

    t = int(round(t/sample_every))
    # print(t)
    [cl.remove() for cl in ax.collections]
    # if hasattr(update_interactive_plot, "cax"):
    #     update_interactive_plot.cax.remove()
    # if hasattr(update_interactive_plot, "sc2"):
    #     update_interactive_plot.sc2.remove()
    # xflat = np.amax(data[t-trange_offset, :], axis=2)
    # #proj_x.contourf(v[0,:,:], w[0,:,:], xflat, cmap=cmap)
    # proj_x.contourf(u[:,0,:], w[:,0,:], xflat, cmap=cmap)
    # proj_x.pcolormesh(u[:,0,:], w[:,0,:], xflat, cmap=cmap)
    ax.grid(False)
    # tmp = ax.pcolormesh(X, Y, xflat)
    plot_parallelogram(ax)
    tmp = ax.scatter(X, Y, c=data[t-trange_offset], edgecolors='black', s=64, cmap='viridis')
    if bump_centers is not None:
        update_interactive_plot.sc2 = ax.scatter(bump_centers[t-trange_offset][:, 0], bump_centers[t-trange_offset][:, 1], c='red', s=64)
    # xmin, ymin, width, height = ax.get_position().bounds
    # update_interactive_plot.cax = fig.add_axes([xmin+width, 0.15, 0.01, 0.7])
    # fig.colorbar(tmp, cax=update_interactive_plot.cax, orientation='vertical')
    # fig, _ = plot_multi(u, v, w, data[t,:].reshape((Nu,Nv,Nw)), th=max_val*th_fact, show_plots=show_plots)


def update_interactive_plot_xproj(fig, ax, data, bump_centers, X, Y, sample_every, trange_offset, t=0):
    """Provides an interactive plot of the time evolution of the activity
    packet. Expects the data as ndarray of shape
    (timepoints, np.prod(resolution_shape)).
    """
    """Remove old contours from plot and plot new one."""

    t = int(round(t/sample_every))
    [cl.remove() for cl in ax.collections]
    if hasattr(update_interactive_plot_xproj, "cax"):
        update_interactive_plot_xproj.cax.remove()
    # if hasattr(update_interactive_plot_xproj, "sc2"):
    #     update_interactive_plot_xproj.sc2.remove()
    ax.grid(False)
    plot_square(ax)
    tmp = ax.scatter(X, Y, c=data[t-trange_offset], edgecolors='black', s=64, cmap='viridis')
    if bump_centers is not None:
        update_interactive_plot_xproj.sc2 = ax.scatter(bump_centers[t-trange_offset][:, 1], bump_centers[t-trange_offset][:, 2], c='red', s=64)
    xmin, ymin, width, height = ax.get_position().bounds
    update_interactive_plot_xproj.cax = fig.add_axes([xmin+width+0.015, 0.115, 0.01, 0.75])
    fig.colorbar(tmp, cax=update_interactive_plot_xproj.cax, orientation='vertical')


def update_interactive_plot_3d(fig, ax, data, bump_centers, X, Y, Z, sample_every, trange_offset, t=0):
    """Provides an interactive plot of the time evolution of the activity
    packet. Expects the data as ndarray of shape
    (timepoints, np.prod(resolution_shape)).
    """
    """Remove old contours from plot and plot new one."""

    t = int(round(t/sample_every))
    [cl.remove() for cl in ax.collections]
    ax.grid(False)
    # tmp = ax.scatter(X, Y, Z, c=data[t-trange_offset], s=64, cmap='viridis', depthshade=True)
    scatter(ax, X, Y, Z, 'navy', data[t-trange_offset].flatten())
    limits = np.array([getattr(ax, f'get_{axis}lim')() for axis in 'xyz'])
    ax.set_box_aspect(np.ptp(limits, axis=1))


def plot_experiment_timeseries(_exp_info, _config, pose_gauss_estimate, time_slice=np.s_[:]):
    sample_every = _config['sample_every']
    simulation_duration = _config['simulation_duration']

    start_time = time_slice.start*sample_every if time_slice.start is not None else 0.0
    stop_time = time_slice.stop*sample_every if time_slice.stop is not None else simulation_duration

    nrow = 3
    ncol = 1

    fig = plt.figure(figsize=(283*_mm, 247*_mm), constrained_layout=True)
    fig.suptitle('Experiment ' + str(_exp_info['_id']) + '  (' + _exp_info['start_time'].isoformat() + ')' + '  [' + str(start_time) + 's - ' + str(stop_time) + 's]')
    gs = GridSpec(nrow, ncol, figure=fig)

    axes = []

    trange = np.arange(0, simulation_duration, sample_every)[time_slice]

    cur_dim = 0
    axes.append(fig.add_subplot(gs[0]))
    plot_pose_estimate_timeseries(trange, pose_gauss_estimate[:, :, cur_dim], None, sample_every, axes[-1], xlim=(0, simulation_duration), ylim=(0, 1.5), ylabel='x')
    cur_dim = 1
    axes.append(fig.add_subplot(gs[1]))
    plot_pose_estimate_timeseries(trange, pose_gauss_estimate[:, :, cur_dim], None, sample_every, axes[-1], xlim=(0, simulation_duration), ylim=(0, sqrt(3)/2), ylabel='y')
    cur_dim = 2
    axes.append(fig.add_subplot(gs[2]))
    plot_pose_estimate_timeseries(trange, pose_gauss_estimate[:, :, cur_dim], None, sample_every, axes[-1], xlim=(0, simulation_duration), ylim=(0, 1), ylabel='z')

    return fig


@plt.style.context(file_dir / 'small.mplstyle')
def plot_experiment_input_phases(_exp_info, _config, bump_centers):
    time_array = get_time_array(_config['input'])

    sample_every = _config['sample_every']
    simulation_duration = _config['simulation_duration']
    grid_shape = _config['grid_shape']
    comment = _config['comment']

    start_time = 0.0
    stop_time = simulation_duration

    nrow = ceil(time_array.shape[0] / 4)
    ncol = time_array.shape[0] if time_array.shape[0] < 5 else 4

    fig = plt.figure(figsize=(_text_width_in, nrow*1.3+0.3), tight_layout=True)  # , constrained_layout=True)
    fig.suptitle('Experiment ' + str(_exp_info['_id']) + '  (' + _exp_info['start_time'].isoformat() + ')' + '  [' + str(start_time) + 's - ' + str(stop_time) + 's]\n' + comment)
    gs = GridSpec(nrow, ncol, figure=fig)

    generators = fspace_base / np.array(grid_shape)
    XXX, YYY, ZZZ = get_3d_coordinates_unwrapped_vectorized(grid_shape, generators)
    XX = XXX[:, :, 0]
    YY = YYY[:, :, 0]

    axes = []

    for index in range(time_array.shape[0]):
        cur_time_range = time_array[index]

        from_idx = round(cur_time_range[0]/sample_every)
        to_idx = round(cur_time_range[1]/sample_every)
        # trange = np.arange(cur_time_range[0], cur_time_range[1], sample_every)

        axes.append(fig.add_subplot(gs[index]))
        ax = axes[-1]
        ax.set_aspect('equal')

        plot_parallelogram(ax)
        plot_hex_grid(ax, XX, YY)
        plot_bump_centers_timeseries(ax, bump_centers[from_idx:to_idx])

        cmd_short_info = ''
        for cmd in _config['input'][index]['cmds']:
            if cmd['cmd'] == 'manual':
                cmd_short_info += 'M{'
                cmd_short_info += 'tr=' + str(cmd['shift_inhib'])  # TODO: use print(f"{var:.3f}")
                cmd_short_info += ', ccw=' + str(cmd['pos_rot_shift_inhib'])
                cmd_short_info += ', cw=' + str(cmd['neg_rot_shift_inhib'])
                cmd_short_info += '}'
            elif cmd['cmd'] == 'input_freq':
                cmd_short_info += 'If{'
                cmd_short_info += str([tuple(x['py/tuple']) for x in cmd['bump_centers']])
                cmd_short_info += '}'
        ax.title.set_text('[' + str(round(cur_time_range[0], 1)) + '-' + str(round(cur_time_range[1], 1)) + ']: ' + cmd_short_info)

    return fig


# https://stackoverflow.com/a/67368551/2868795
def num(s):
    """ 3.0 -> 3, 3.001000 -> 3.001 otherwise return s """
    s = str(s)
    try:
        int(float(s))
        return s.rstrip('0').rstrip('.')
    except ValueError:
        return s


@plt.style.context(file_dir / 'regular.mplstyle')
# @plt.style.context(file_dir / 'small.mplstyle')  # 4 column width
def plot_experiment_xy(_exp_info, _config, bump_centers, time_slice=np.s_[:]):
    grid_shape = _config['grid_shape']
    sample_every = _config['sample_every']
    simulation_duration = _config['simulation_duration']  # float(28.3)

    start_time = time_slice.start*sample_every if time_slice.start is not None else 0.0
    stop_time = time_slice.stop*sample_every if time_slice.stop is not None else simulation_duration
    plotted_duration = stop_time - start_time
    # trange = np.arange(0, simulation_duration, sample_every)[time_slice]

    nrow = 1
    ncol = 1

    fig = plt.figure(figsize=(_column_width_in, _column_width_in*0.577350+0.028), constrained_layout=True)  # column width
    # fig = plt.figure(figsize=(_4column_width_in, _4column_width_in*0.577350+0.0252), constrained_layout=True)  # 4 column width
    # fig = plt.figure(figsize=(_column_width_in, _column_width_in*0.577350+0.008), constrained_layout=True)  # column width -- OLD
    # fig.suptitle('Experiment ' + str(_exp_info['_id']) + '  (' + _exp_info['start_time'].isoformat() + ')' + '  [' + str(start_time) + 's - ' + str(stop_time) + 's]')
    gs = GridSpec(nrow, ncol, figure=fig)

    axes = []
    axes.append(fig.add_subplot(gs[0]))
    ax = axes[-1]
    ax.set_aspect('equal')

    ax.set_xlim(-0.0091, 1.5091)  # column width
    ax.set_ylim(-0.0091, sqrt(3)/2+0.0091)  # column width
    # ax.set_xlim(-0.0306, 1.5+0.0306)  # 4 column width
    # ax.set_ylim(-0.0306, sqrt(3)/2+0.0306)  # 4 column width
    # ax.set_xlim(-0.006, 1.505)  # column width -- OLD
    # ax.set_ylim(-0.006, sqrt(3)/2+0.003)  # column width -- OLD

    # ax.spines['left'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['top'].set_visible(False)

    # ax.tick_params(left=False, bottom=False)

    ax.axis('off')

    generators = fspace_base / np.array(grid_shape)
    XXX, YYY, ZZZ = get_3d_coordinates_unwrapped_vectorized(grid_shape, generators)
    XX = XXX[:, :, 0]
    YY = YYY[:, :, 0]

    plot_parallelogram(ax)
    plot_hex_grid(ax, XX, YY, s=1, facecolor='black')  # column width
    # plot_hex_grid(ax, XX, YY, s=0.3, facecolor='black')  # 4 column width
    plot_bump_centers_timeseries(ax, bump_centers[time_slice])  # column width
    # plot_bump_centers_timeseries(ax, bump_centers[time_slice], s=1.5**2)  # 4 column width

    # ax.scatter(x=0, y=0, color='blue')
    # ax.scatter(x=1.5, y=sqrt(3)/2, color='blue')

    # colorbar
    cmap = mpl.cm.get_cmap('rainbow')
    # Normalizer
    norm = mpl.colors.Normalize(vmin=0, vmax=plotted_duration)

    # creating ScalarMappable
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # axins = inset_axes(ax,
    #                    width='3%',
    #                    height='60%',
    #                    loc='lower right',
    #                    borderpad=1)
    axins = ax.inset_axes([0.968, 0.0103, 0.03, 0.6])  # column width
    # axins = ax.inset_axes([0.968-0.015, 0.0335, 0.03, 0.5])  # 4 column width
    # axins = ax.inset_axes([0.968, 0.007, 0.03, 0.6])  # column width -- OLD

    cbar = fig.colorbar(sm, cax=axins, orientation='vertical')
    cbar.ax.yaxis.set_ticks_position('left')
    # cbar.ax.set_yticks([0, 2.5, 5])
    # cbar.ax.set_yticklabels(['0s', '2.5s', '5s'])
    cbar.ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(2.5))  # column width
    # cbar.ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(3))  # 4 column width
    fmt = lambda x, pos: num(x) + 's'
    cbar.ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(fmt))
    for idx, tick in enumerate(cbar.ax.yaxis.get_majorticklabels()):
        # there appear to be extra entries in the list...
        if idx < 2:
            tick.set_verticalalignment("bottom")
            tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, -0.0315, fig.dpi_scale_trans))  # column width
            # tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, -0.027, fig.dpi_scale_trans))  # 4 column width
        elif idx > len(cbar.ax.yaxis.get_majorticklabels())-3:
            tick.set_verticalalignment("top")
            tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, 0.011, fig.dpi_scale_trans))  # column width
            # tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, 0.0103, fig.dpi_scale_trans))  # 4 column width

    # axins_angle = ax.inset_axes([0.002, 0.83, 0.25, 0.17])
    # num_timepoints = len(bump_centers[time_slice])
    # for t in range(num_timepoints):
    #     axins_angle.scatter(x=t/num_timepoints*plotted_duration*np.ones(bump_centers[time_slice][t].shape[0]), y=bump_centers[time_slice][t][:, 2], s=0.5, color='black')
    # axins_angle.set_xlim(0, plotted_duration)

    fig.set_constrained_layout_pads(w_pad=0, h_pad=0, hspace=0, wspace=0)
    # plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig


@plt.style.context(file_dir / 'regular.mplstyle')
def plot_experiment_xy_trajectories(traj_target, traj_actual, start_time, stop_time):
    # plotted_duration = stop_time - start_time

    nrow = 1
    ncol = 1

    fig = plt.figure(figsize=(_column_width_in, _column_width_in-0.02), constrained_layout=True)  # irat
    # fig = plt.figure(figsize=(_column_width_in, _column_width_in*1.5+0.45), constrained_layout=True)  # robotcar
    gs = GridSpec(nrow, ncol, figure=fig)

    axes = []
    axes.append(fig.add_subplot(gs[0]))
    ax = axes[-1]
    ax.set_aspect('equal')

    ax.set_xlim(-1.2, 1.7)  # irat
    ax.set_ylim(-0.7, 3.2)  # irat
    # ax.set_xlim(-0.2, 1.7)  # robotcar
    # ax.set_ylim(-4.2, 0.2)  # robotcar

    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.5))

    ax.set_xlabel('x (u)')
    ax.set_ylabel('y (u)')

    # ax.spines['left'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['top'].set_visible(False)
    # ax.tick_params(left=False, bottom=False)
    # ax.axis('off')

    cmap = mpl.cm.get_cmap('rainbow')
    norm = mpl.colors.Normalize(vmin=start_time, vmax=stop_time)

    # target trajectory
    # adapted from: https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
    points = np.vstack((traj_target[:, 0], traj_target[:, 1])).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=cmap, norm=norm, label='target')
    lc.set_array(traj_target[:, 2])
    lc.set_linewidth(1.4)
    ax.add_collection(lc)

    ax.scatter(traj_target[:, 0], traj_target[:, 1], c=traj_target[:, 2], cmap=cmap, s=1.4**2, linewidth=0, zorder=2)

    # actual trajectory
    ax.scatter(traj_actual[:, 0], traj_actual[:, 1], c=traj_actual[:, 2], cmap=cmap, s=3**2, linewidth=0, label='actual', zorder=2)

    # colorbar
    # creating ScalarMappable
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="6%", pad=0.1)
    cbar = fig.colorbar(sm, cax=cax)
    # cbar.ax.yaxis.set_ticks_position('left')
    # cbar.ax.set_yticks([0, 2.5, 5])
    # cbar.ax.set_yticklabels(['0s', '2.5s', '5s'])
    # cbar.ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(2.5))
    fmt = lambda x, pos: num(x) + 's'
    cbar.ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(fmt))
    for idx, tick in enumerate(cbar.ax.yaxis.get_majorticklabels()):
        # there appear to be extra entries in the list...
        if idx < 1:
            tick.set_verticalalignment("bottom")
            tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, -0.0315, fig.dpi_scale_trans))

    # legend
    from matplotlib.lines import Line2D
    target_legend = Line2D([0], [0], linewidth=1.4, color='black')
    actual_legend = Line2D([0], [0], linestyle='none', marker='o', markersize=3, color='black')
    ax.legend((target_legend, actual_legend), ('target', 'actual'), bbox_to_anchor=(0.95, 0.95), loc='upper right', frameon=False, borderpad=0, borderaxespad=0, handletextpad=0.6, handlelength=1.2)  # irat
    # ax.legend((target_legend, actual_legend), ('target', 'actual'), bbox_to_anchor=(0.1, 0.5), loc='center left', frameon=False, borderpad=0, borderaxespad=0, handletextpad=0.6, handlelength=1.2)  # robotcar

    fig.set_constrained_layout_pads(w_pad=0, h_pad=0, hspace=0, wspace=0)
    # plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig


@plt.style.context(file_dir / 'small.mplstyle')
def plot_experiment_xy_sliced(_exp_info, _config, bump_centers, label_text, label_positions, offset_from_data_start, time_slice=np.s_[:]):
    grid_shape = _config['grid_shape']
    sample_every = _config['sample_every']
    simulation_duration = _config['simulation_duration']  # float(28.3)

    start_time = (time_slice.start*sample_every if time_slice.start is not None else 0.0) - offset_from_data_start
    stop_time = (time_slice.stop*sample_every if time_slice.stop is not None else simulation_duration) - offset_from_data_start

    simulation_duration = simulation_duration - offset_from_data_start

    nrow = 1
    ncol = 1

    fig = plt.figure(figsize=(_4column_width_in, _4column_width_in*0.577350+0.0252), constrained_layout=True)
    gs = GridSpec(nrow, ncol, figure=fig)

    axes = []
    axes.append(fig.add_subplot(gs[0]))
    ax = axes[-1]
    ax.set_aspect('equal')

    ax.set_xlim(-0.0306, 1.5+0.0306)  # 4 column width
    ax.set_ylim(-0.0306, sqrt(3)/2+0.0306)  # 4 column width

    ax.axis('off')

    generators = fspace_base / np.array(grid_shape)
    XXX, YYY, ZZZ = get_3d_coordinates_unwrapped_vectorized(grid_shape, generators)
    XX = XXX[:, :, 0]
    YY = YYY[:, :, 0]

    plot_parallelogram(ax)
    plot_hex_grid(ax, XX, YY, s=0.3, facecolor='black')
    color_slice_start = start_time / simulation_duration
    color_slice_end = stop_time / simulation_duration
    plot_bump_centers_timeseries_sliced(ax, bump_centers[time_slice], color_slice_start=color_slice_start, color_slice_end=color_slice_end, s=1.5**2)

    for label_idx in np.arange(0, len(label_text)):
        ax.text(label_positions[label_idx][0], label_positions[label_idx][1], label_text[label_idx])

    # colorbar
    # https://stackoverflow.com/a/18926541/2868795
    import matplotlib.colors as colors
    def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=1000):
        new_cmap = colors.LinearSegmentedColormap.from_list(
            'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
            cmap(np.linspace(minval, maxval, n)))
        return new_cmap
    cmap = mpl.cm.get_cmap('rainbow')
    cmap = truncate_colormap(cmap, color_slice_start, color_slice_end)

    # Normalizer
    norm = mpl.colors.Normalize(vmin=start_time, vmax=stop_time)

    # creating ScalarMappable
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    axins = ax.inset_axes([0.968-0.015, 0.0335, 0.03, 0.4])

    cbar = fig.colorbar(sm, cax=axins, orientation='vertical')
    cbar.ax.yaxis.set_ticks_position('left')
    cbar.ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(2.5))
    fmt = lambda x, pos: num(x) + 's'
    cbar.ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(fmt))
    for idx, tick in enumerate(cbar.ax.yaxis.get_majorticklabels()):
        # there appear to be extra entries in the list...
        if idx < 2:
            tick.set_verticalalignment("bottom")
            tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, -0.027, fig.dpi_scale_trans))
        elif idx > len(cbar.ax.yaxis.get_majorticklabels())-3:
            tick.set_verticalalignment("top")
            tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, 0.0103, fig.dpi_scale_trans))

    fig.set_constrained_layout_pads(w_pad=0, h_pad=0, hspace=0, wspace=0)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig


@plt.style.context(file_dir / 'regular.mplstyle')
def plot_experiment_orientation_over_time(_exp_info, _config, bump_centers, time_slice=np.s_[:]):
    grid_shape = _config['grid_shape']
    sample_every = _config['sample_every']
    simulation_duration = _config['simulation_duration']

    start_time = time_slice.start*sample_every if time_slice.start is not None else 0.0
    stop_time = time_slice.stop*sample_every if time_slice.stop is not None else simulation_duration
    plotted_duration = stop_time - start_time
    trange = np.arange(0, simulation_duration, sample_every)[time_slice]

    nrow = 1
    ncol = 1

    fig = plt.figure(figsize=(_column_width_in, _column_width_in*0.577350+0.008), constrained_layout=True)
    gs = GridSpec(nrow, ncol, figure=fig)

    axes = []
    axes.append(fig.add_subplot(gs[0]))
    ax = axes[-1]

    ax.yaxis.grid(True, which='major', linewidth=0.4, color='black')
    ax.yaxis.grid(True, which='minor', linewidth=0.2, color='black')

    num_timepoints = len(bump_centers[time_slice])
    for t in range(num_timepoints):
        ax.scatter(x=t/num_timepoints*plotted_duration*np.ones(bump_centers[time_slice][t].shape[0]), y=bump_centers[time_slice][t][:, 2]*2*pi, s=0.5, color='black')
    ax.set_xlim(0, plotted_duration)
    ax.set_ylim(0, 2*pi)

    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Orientation Angle')

    ax.set_yticks([0, pi/2, pi, 3*pi/2, 2*pi])
    # ax.set_yticks([0, pi, 2*pi])
    ax.set_yticklabels(['0', '90', '180', '270', '360'])
    # ax.set_yticklabels(['0', r'$\pi$', r'$2\pi$'])

    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(pi/8))

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    fig.set_constrained_layout_pads(w_pad=0, h_pad=0.01, hspace=0, wspace=0)
    # plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig


# @plt.style.context(file_dir / 'small.mplstyle')
def plot_bump_centers_timeseries(ax, bump_centers, **kwargs):
    num_timepoints = len(bump_centers)

    cmap = mpl.cm.get_cmap('rainbow')
    colors = cmap(np.mgrid[0:1:(num_timepoints * 1j)])
    for t in range(num_timepoints):
        ax.scatter(x=bump_centers[t][:, 0], y=bump_centers[t][:, 1], color=colors[t], **kwargs)


def plot_bump_centers_timeseries_sliced(ax, bump_centers, color_slice_start, color_slice_end, **kwargs):
    num_timepoints = len(bump_centers)

    cmap = mpl.cm.get_cmap('rainbow')
    colors = cmap(np.mgrid[color_slice_start:color_slice_end:(num_timepoints * 1j)])
    for t in range(num_timepoints):
        ax.scatter(x=bump_centers[t][:, 0], y=bump_centers[t][:, 1], color=colors[t], **kwargs)


@plt.style.context(file_dir / 'small.mplstyle')
def plot_experiment_snapshot_reconstructed_xy(grid_shape, pose_reconstructed, bump_centers, vmin=0., vmax=0.):
    data = np.amax(pose_reconstructed, axis=2)
    if vmin == 0. and vmax == 0.:
        vmin = data.min()
        vmax = data.max()

    nrow = 1
    ncol = 1

    fig = plt.figure(figsize=(_4column_width_in, _4column_width_in*0.577350+0.0252), constrained_layout=True)
    gs = GridSpec(nrow, ncol, figure=fig)

    axes = []
    axes.append(fig.add_subplot(gs[0]))
    ax = axes[-1]

    ax.set_xlim(-0.0306, 1.5+0.0306)
    ax.set_ylim(-0.0306, sqrt(3)/2+0.0306)
    ax.axis('off')
    ax.set_aspect('equal')

    generators = fspace_base / np.array(grid_shape)
    XXX, YYY, ZZZ = get_3d_coordinates_unwrapped_vectorized(grid_shape, generators)
    XX = XXX[:, :, 0]
    YY = YYY[:, :, 0]

    plot_parallelogram(ax)

    # reconstructed pose estimate surface
    ax.scatter(XX, YY, c=data, cmap='viridis_r', s=16, edgecolor='black', linewidth=0.3, vmin=vmin, vmax=vmax)

    # computed bump centers
    ax.scatter(x=bump_centers[:, 0], y=bump_centers[:, 1], color='red', edgecolor='red', linewidth=0.3, s=16)

    # colorbar
    cmap = mpl.cm.get_cmap('viridis_r')
    # Normalizer
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

    # creating ScalarMappable
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    axins = ax.inset_axes([0.968-0.015, 0.0335, 0.03, 0.4])

    cbar = fig.colorbar(sm, cax=axins, orientation='vertical', ticks=[vmin, vmax])
    cbar.ax.yaxis.set_ticks_position('left')
    fmt = lambda x, pos: round(x, 2)
    cbar.ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(fmt))
    for idx, tick in enumerate(cbar.ax.yaxis.get_majorticklabels()):
        if idx == 0:
            tick.set_verticalalignment("bottom")
            tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, -0.027, fig.dpi_scale_trans))
        elif idx == 1:
            tick.set_verticalalignment("top")
            tick.set_transform(tick.get_transform() + mpl.transforms.ScaledTranslation(0, 0.0103, fig.dpi_scale_trans))

    fig.set_constrained_layout_pads(w_pad=0, h_pad=0, hspace=0, wspace=0)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig



def plot_fourier_coefs_2d(ax_arr, fc_arr):
    # ax_arr: axes array
    # fc_arr: Fourier coefficient array

    assert(ax_arr.shape == fc_arr.shape)

    for index, x in np.ndenumerate(fc_arr):
        ax_arr[index].plot([0, np.angle(x)], [0, abs(x)], marker='o')


def plot_fourier_coefs_3d_multi(data, figtitle=''):
    # data: array of arrays of fourier coefs, shape=(num_arrays, *fgrid_shape)

    fgrid_shape = data.shape[1:]

    num_coefarrs = data.shape[0]

    num_subfigrows = fgrid_shape[2]
    num_subfigcols = 1

    num_rowspersubfig = fgrid_shape[0]
    num_colspersubfig = fgrid_shape[1]

    fig = plt.figure(figsize=(2*_text_width_in, num_subfigrows*num_rowspersubfig*1.7+0.2), constrained_layout=True)
    fig.suptitle(figtitle)
    subfigs = np.atleast_1d(fig.subfigures(nrows=num_subfigrows, ncols=num_subfigcols))

    for w in range(num_subfigrows):
        subfig = subfigs[w]
        subfig.suptitle(f'z={w}')
        axes = subfig.subplots(nrows=num_rowspersubfig, ncols=num_colspersubfig, subplot_kw=dict(projection='polar'))
        axes = axes.reshape((num_rowspersubfig, num_colspersubfig))

        for i in range(num_coefarrs):
            plot_fourier_coefs_2d(axes, data[i, :, :, w])

        # if idx_x == 0 and idx_y == 0:
        #     plt.legend(['000', 'other'], loc='upper left')


def plot_experiment_interactive(title, sample_every, simulation_duration, XXX, YYY, ZZZ, pose_reconstructed, bump_centers=None, time_slice=np.s_[:]):
    XX_zproj = XXX[:, :, 0]
    YY_zproj = YYY[:, :, 0]
    YY_xproj = YYY[0, :, :]
    ZZ_xproj = ZZZ[0, :, :]

    start_time = time_slice.start*sample_every if time_slice.start is not None else 0.0
    stop_time = time_slice.stop*sample_every if time_slice.stop is not None else simulation_duration

    data = []
    data.append(np.amax(pose_reconstructed, axis=3))
    data.append(np.amax(pose_reconstructed, axis=1))
    data.append(pose_reconstructed.copy())
    data[-1] *= 1.0/data[-1].max(axis=(1, 2, 3)).reshape((data[-1].shape[0], 1, 1, 1))
    data[-1][data[-1] < 0] = 0

    nrow = 1
    ncol = 3

    fig = plt.figure(figsize=(_page_height_in, 3), constrained_layout=True)  # , tight_layout=True)
    fig.suptitle(title + '  [' + str(start_time) + 's - ' + str(stop_time) + 's]')
    # fig.suptitle('Experiment ' + str(_exp_info['_id']) + '  (' + _exp_info['start_time'].isoformat() + ')' + '  [' + str(start_time) + 's - ' + str(stop_time) + 's]')
    gs = GridSpec(nrow, ncol, figure=fig)

    axes = []

    trange = np.arange(0, simulation_duration, sample_every)[time_slice]

    axes.append(fig.add_subplot(gs[0]))
    axes[-1].set_title('project z')
    axes[-1].set_xlabel('x')
    axes[-1].set_ylabel('y')
    axes[-1].set_aspect('equal', 'box')
    axes.append(fig.add_subplot(gs[1]))
    axes[-1].set_title('project x')
    axes[-1].set_xlabel('y')
    axes[-1].set_ylabel('z')
    axes[-1].set_aspect('equal', 'box')
    axes.append(fig.add_subplot(gs[2], projection='3d'))
    axes[-1].set_xlabel('x')
    axes[-1].set_ylabel('y')
    axes[-1].set_zlabel('z')

    # XXX, YYY, ZZZ = get_3d_coordinates_unwrapped_vectorized(fourier_coef_shape, fourier_generators)
    tmp_func = lambda t: update_interactive_plot_wrapper(fig, axes, XXX, YYY, ZZZ, XX_zproj, YY_zproj, YY_xproj, ZZ_xproj, data, bump_centers, sample_every, trange_offset=(time_slice.start if time_slice.start is not None else 0), t=t)  # noqa: E731

    # widgets.interact(
    #     tmp_func,
    #     t=widgets.FloatSlider(
    #         value=trange[0],
    #         min=trange[0],
    #         max=trange[-1],
    #         step=sample_every,
    #         layout=widgets.Layout(width='512px')))

    float_slider_params = {
        'value': trange[0],
        'min': trange[0],
        'max': trange[-1],
        'step': sample_every
    }

    return fig, tmp_func, float_slider_params


@plt.style.context(file_dir / 'regular.mplstyle')
def setup_weights_plot(neuron_res):
    # fig = plt.figure(figsize=(_column_width_in*0.7643563062780397, _column_width_in*0.7643563062780397), constrained_layout=True)
    fig = plt.figure(figsize=(_column_width_in, _column_width_in), constrained_layout=True)
    ax = plt.axes()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.0001, 0.0007)
    # ax.scatter(np.arange(0, 1, 1/neuron_res) - 0.5, np.zeros(neuron_res), label='neurons', c='black')

    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.25))
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1/neuron_res))
    ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.0001))

    # ax.spines['left'].set_position('zero')
    ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)

    ax.axhline(0, color='black', linestyle='dashed', linewidth=mpl.rcParams['axes.linewidth'])
    ax.axvline(0, color='black', linestyle='dashed', linewidth=mpl.rcParams['axes.linewidth'])

    ax.set_xlabel('Distance from origin')
    ax.set_ylabel('Magnitude')

    yfmt = ScalarFormatter()
    yfmt.set_powerlimits((0, 0))
    ax.yaxis.set_major_formatter(yfmt)
    ax.yaxis.labelpad = -2

    fig.set_constrained_layout_pads(w_pad=0, h_pad=0.01, hspace=0, wspace=0)

    return fig, ax


# @plt.style.context(['seaborn-paper', file_dir / 'regular.mplstyle'])
# @plt.style.context('seaborn-paper')
@plt.style.context(file_dir / 'regular.mplstyle')
def get_weights_plot(popts, labels, neuron_res):
    fig, ax = setup_weights_plot(neuron_res)
    prop = ax._get_lines.prop_cycler

    reso_mex_hat = 100
    pos_mex_hat = np.zeros((reso_mex_hat, 3))
    pos_mex_hat[:, 0] = np.mgrid[-0.5:0.5:(reso_mex_hat * 1j)]

    neuron_positions = np.zeros((neuron_res, 3))
    neuron_positions[:, 0] = np.arange(0, 1, 1/neuron_res) - 0.5

    # popt_raw = np.array([0.0116805552, 0.0116910095, 1.00150796, 1.00115252, 0])  # exp 1154
    # gauss_mex_hat_raw = mex_hat(pos_mex_hat, *popt_raw)
    # ax.plot(pos_mex_hat[:,0], gauss_mex_hat_raw, label='raw', c='black', linestyle='dotted')

    # popt = np.array([weight_config['var_exc'], weight_config['var_inh'], weight_config['fact_exc'], weight_config['fact_inh'], weight_config['offset']])
    for i in range(len(popts)):
        color = next(prop)['color']
        gauss_mex_hat = mex_hat(pos_mex_hat, *popts[i])
        ax.plot(pos_mex_hat[:, 0], gauss_mex_hat, color=color, label=labels[i])
        neuron_values = mex_hat(neuron_positions, *popts[i])
        ax.scatter(neuron_positions[:, 0], neuron_values, color=color)
        # ax.plot([], [], '-o', color=color, label=labels[i])

    ax.legend(bbox_to_anchor=(1, 1), loc='upper right', frameon=False, borderpad=0, borderaxespad=0)

    return fig, ax


# https://github.com/osnove/other/blob/master/complex_plane.py
# def complex_plane2(z,axis_type=0):
#     """Creates complex plane and shows complex numbers as vectors (complexors)

#     Parameters
#     ----------
#     z : array of complex values
#         array of complex values to be shown
#     axis_type : int
#         three types of shapes of complex plane:
#         0 : symple
#         1 : with grid
#         2 : moved axis to middle
#     -----------------------------------
#     # Example
#     z=[20+10j,15,-10-10j,5+15j]
#     complex_plane2(z,2) """

#     w=max(np.abs(z))
#     fig, ax = plt.subplots()

#     if axis_type==0:
#         plt.axis("off")
#         plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
#         plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
#     elif axis_type==1:
#         plt.axis("on")
#         plt.grid()
#         plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
#         plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
#     else:
#          # Move left y-axis and bottim x-axis to centre, passing through (0,0)
#         ax.spines['left'].set_position('center')
#         ax.spines['bottom'].set_position('center')

#         # Eliminate upper and right axes
#         ax.spines['right'].set_color('none')
#         ax.spines['top'].set_color('none')

#         # Show ticks in the left and lower axes only
#         ax.xaxis.set_ticks_position('bottom')
#         ax.yaxis.set_ticks_position('left')

#         ax.set_xlabel('                                                 Re []')
#         ax.set_ylabel('                                                 Im []')

#     plt.xlim(-w,w)
#     plt.ylim(-w,w)
#     plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k');
#     plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k');

#     for i in range(len(z)):
#         fi_a=np.angle(z[i])
#         x=z[i].real -abs(w)/20*np.cos(fi_a)
#         y=z[i].imag-abs(w)/20*np.sin(fi_a)
#         plt.arrow(0, 0, x, y, head_width=w/20, head_length=w/20, fc='b', ec='b');
#     plt.show()
