"""
Generation and preprocessing of input data, conversion between velocities and inhibition values, as
well as trajectory-related functions.
"""
from collections.abc import Callable
import logging
from math import ceil, pi
import numpy as np
import numpy.typing as npt

from pose.hex import get_domain
from pose.freq_space import (
    get_0_coefs,
    get_rotation_matrix
)
import pose.nengo_utils
from pose.typing import GridShape

logger = logging.getLogger(__name__)


# def getf_input_pose(dim_pose, fourier_coef_shape, cov, scale_fact, init_period, crop_conj_sym=False):
#     gauss0_f_cropped_flat = get_0_coefs(fourier_coef_shape, cov, crop_conj_sym)

#     def input_pose(t, x):
#         out = np.zeros(dim_pose)

#         if t < init_period:
#             center = get_domain() * np.array([0, 0, 0]) / np.array(fourier_coef_shape)
#             rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#             coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#             out = coefs_cropped_flat
#             out *= scale_fact

#             center2 = get_domain() * np.array([4, 4, 4]) / np.array(fourier_coef_shape)
#             rot_mat2 = rot_mat_cropped_abelian(fourier_coef_shape, center2, crop_conj_sym)
#             coefs_cropped_flat2 = rot_mat2.dot(gauss0_f_cropped_flat)
#             out2 = coefs_cropped_flat2
#             out2 *= scale_fact

#             out = out + out2
#         elif t >= 31 and t < 31 + init_period:
#             center = get_domain() * np.array([0, 0, 0.5]) / np.array(fourier_coef_shape)
#             rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#             coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#             out = coefs_cropped_flat
#             out *= scale_fact
#         elif t >= 52 and t < 52 + init_period:
#             center = get_domain() * np.array([0, 0, 1]) / np.array(fourier_coef_shape)
#             rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#             coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#             out = coefs_cropped_flat
#             out *= scale_fact
#         # out -= x
#         # elif t >= 30 and t < 30 + init_period:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 0.5*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 45 and t < 45 + init_period:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 0.75*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 60 and t < 60 + init_period:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 1*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 75 and t < 75 + init_period:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 2*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 90 and t < 90 + init_period:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 0*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 20 and t < 23:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 2*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 30 and t < 33:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 3*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 40 and t < 43:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 4*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 50 and t < 53:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 5*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 60 and t < 63:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 6*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 70 and t < 73:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 7*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 80 and t < 81:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 0*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 90 and t < 91:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 0*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 100 and t < 101:
#         #     center = np.array([0*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 0*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         # elif t >= 5 and t < 6:
#         #     # center = np.array([domain[0]/fourier_coef_shape[0], domain[1]/fourier_coef_shape[1], 0.0])  # / np.array(neuron_shape)
#         #     center = np.array([1*domain[0]/fourier_coef_shape[0], 1*domain[1]/fourier_coef_shape[1], 2*domain[2]/fourier_coef_shape[2]])
#         #     # center = np.zeros(3)
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         #     # out -= x
#         # elif t >= 10 and t < 11:
#         #     center = np.array([3*domain[0]/fourier_coef_shape[0], 0*domain[1]/fourier_coef_shape[1], 3*domain[2]/fourier_coef_shape[2]])
#         #     rot_mat = rot_mat_cropped_abelian(fourier_coef_shape, center, crop_conj_sym)
#         #     coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
#         #     out = coefs_cropped_flat
#         #     out *= scale_fact
#         else:
#             1

#         return out

#     return input_pose


# def getf_shift_inhib(dt, init_period):
#     # trajectory = np.load('debug/npy/trajectory_circular_1.npy')

#     def shift_inhib(t):
#         out = 0

#         interval_speed = 7  # every interval_speed timesteps

#         if t < init_period:
#             out = 1
#         elif t >= 31 and t < 31 + init_period:
#             out = 1
#         elif t >= 52 and t < 52 + init_period:
#             out = 1
#         # elif t >= 15 and t < 15 + init_period:
#         #     out = 1
#         # elif t >= 30 and t < 30 + init_period:
#         #     out = 1
#         # elif t >= 45 and t < 45 + init_period:
#         #     out = 1
#         # elif t >= 60 and t < 60 + init_period:
#         #     out = 1
#         # elif t >= 75 and t < 75 + init_period:
#         #     out = 1
#         # elif t >= 20 and t < 23:
#         #     out = 1
#         # elif t >= 30 and t < 33:
#         #     out = 1
#         # elif t >= 40 and t < 43:
#         #     out = 1
#         # elif t >= 50 and t < 53:
#         #     out = 1
#         # elif t >= 60 and t < 63:
#         #     out = 1
#         # elif t >= 70 and t < 73:
#         #     out = 1
#         # elif t >= 80 and t < 101:
#         #     out = 1
#         # elif t >= 101:
#         #     if abs((t/dt) % 2) - 0 < 1e-5:  # shift's turn
#         #         tmp = (t/dt + 2) / 2
#         #         if abs(tmp % 5) < 1e-5:
#         #             out = 1
#         # elif t >= 90:
#         #     out = 1
#         else:
#             # if abs((t/dt) % 2) - 0 < 1e-5:  # shift's turn
#             #     tmp = (t/dt + 2) / 2
#             #     if abs(tmp % interval_speed) < 1e-5:
#             #         out = 1
#             #     # out = 1/6
#             # out = 1/12
#             idx = round(t / 0.001) - 1000
#             out = 0.05  # trajectory[idx, 0]

#         return out

#     return shift_inhib


# def getf_rotate_pos_inhib(dt, init_period):
#     # trajectory = np.load('debug/npy/trajectory_circular_1.npy')

#     def rotate_pos_inhib(t):
#         out = 0

#         interval_speed = 3  # every interval_speed timesteps

#         if t < init_period:
#             out = 1
#         elif t >= init_period and t < 31:
#             out = 0.03
#         elif t >= 31 and t < 31 + init_period:
#             out = 1
#         elif t >= 52 and t < 52 + init_period:
#             out = 1
#         # if t < 95:
#         #     out = 1
#         # elif t >= 90 and t < 101:
#         #     out = 1
#         # elif t >= 101:
#         #     if abs((t/dt) % 2) - 1 < 1e-5:  # rotate's turn
#         #         tmp = (t/dt + 1) / 2
#         #         if abs(tmp % 3) < 1e-5:
#         #             out = 1
#         else:
#             # if abs((t/dt) % 2) - 1 < 1e-5:  # rotate's turn
#             #     tmp = (t/dt + 1) / 2
#             #     if abs(tmp % interval_speed) < 1e-5:
#             #         out = 1
#             #     # out = 1/5
#             # out = 1/6
#             idx = round(t / 0.001) - 1000
#             # out = 0.05#trajectory[idx, 1]
#             out = 1

#         return out

#     return rotate_pos_inhib


# def getf_rotate_neg_inhib(dt, init_period):
#     def rotate_neg_inhib(t):
#         out = 0

#         # interval_speed = 5  # every interval_speed timesteps

#         # if t < 91:
#         #     out = 1
#         # elif t >= 100:
#         #     out = 1
#         # else:
#         #     if abs((t/dt) % 2) - 1 < 1e-5:  # rotate's turn
#         #         tmp = (t/dt + 1) / 2
#         #         if abs(tmp % interval_speed) < 1e-5:
#         #             out = 1

#         out = 1

#         return out

#     return rotate_neg_inhib


# def func_to_fit(data, a, b, c, d, f):
#     x, y = data
#     return a*x*x + b*x + c*y*y + d*y + f


# def func_to_fit4(data, a, b, c, d, e, f, g):
#     x, y = data
#     arg = x-f*np.exp(y)+g
#     return a*arg*arg*arg*arg + b*arg*arg*arg + c*arg*arg + d*arg + e


# def func_to_fit4_ang(data, a, b, c, d, e, f, g):
#     x, y = data
#     arg = y-f*np.exp(x)+g
#     return a*arg*arg*arg*arg + b*arg*arg*arg + c*arg*arg + d*arg + e


# def func_to_fit5(data, a, b, c, d, e):
#     x, y = data
#     arg = np.exp(x)-e*np.exp(y)
#     return a*arg*arg + b*arg + c + d*np.exp(y)


# def func_to_fit5_ang(data, a, b, c, d, e):
#     x, y = data
#     arg = y-e*x
#     return a*arg*arg + b*arg + c + d*x


def func_to_fit3(data, a, b, c, d, e, f, g):
    """Generic 3rd-order bivariate polynomial function."""
    x, y = data
    arg = x
    return a*arg*arg*arg + b*arg*arg + c*arg + d + e*y*y*y + f*y*y + g*y


# curve_fit
# coefs_shift_inhib = np.array([-0.6993618, -0.08314648, -0.00305444, 0.00471629, 0.0350983, 0.05269146])
# coefs_rotation_inhib = np.array([0.18286141, -0.02258806, -0.01276425, -0.0188628, -0.01428225, 0.05742897])

# sheets trendline
# coefs_shift_inhib = np.array([-0.583, -0.0787, 0., 0., 0., 0.0553])
# coefs_rotation_inhib = np.array([0., 0., -0.0135, -0.0191, 0., 0.058])

# other independent variable has only linear influence
# coefs_shift_inhib = np.array([-0.63622041, -0.06724485, 0., 0.00450185, 0., 0.05073282])
# coefs_rotation_inhib = np.array([0., 0.01775775, -0.01306583, -0.02034884, 0., 0.05595276])

# 4th order polynomial with modified arguments
# coefs_shift_inhib = np.array([-4.57383693e+01, 3.13558545e+00, -4.61704656e-02, -2.08560005e-01, 4.15860312e-02, 6.39065695e-03, -7.85751390e-02])
# coefs_rotation_inhib = np.array([-0.01353956, 0.08026541, -0.17033977, 0.11184542, 0.05900398, 0.23640688, 1.30651178])

# [working well] 3rd order bivariate polynomial; with edgecases
# coefs_shift_inhib = np.array([-3.4982933, 0.88360055, -0.26181309, 0.05958984, -0.00525118, 0.0134452, -0.00538486])
# coefs_rotation_inhib = np.array([1.85133178, -0.62603038, 0.06773443, 0.06800798, -0.02541713, 0.05451435, -0.07438908])

# [working well] 3rd order bivariate polynomial; with all edgecases; outliers removed individually for tang and ang cases
coefs_shift_inhib = np.array([-5.12789881, 1.63221362, -0.364301, 0.06376009, -0.00529229, 0.01347963, -0.00594336])
"""Coefficients for computing shift inhibition from velocity with `func_to_fit3`, as obtained by
fitting hand-labeled simulation data, where all edgecases are included and outliers removed.
"""
coefs_rotation_inhib = np.array([2.24429458, -0.83483308, 0.0996706, 0.06562274, -0.02284753, 0.04700435, -0.06818754])
"""Coefficients for computing rotation inhibition from velocity with `func_to_fit3`, as obtained by
fitting hand-labeled simulation data, where all edgecases are included and outliers removed.
"""

# def vel_to_inhib(tangential_vel, angular_vel):
#     shift_inhib = func_to_fit((tangential_vel, angular_vel), *coefs_shift_inhib)
#     rotation_inhib = func_to_fit((tangential_vel, angular_vel), *coefs_rotation_inhib)
#     return (shift_inhib, rotation_inhib)


max_tang_vel = 0.223
"""Maximum tangential velocity that can be represented by the pose network. Valid for any angular
velocity up to `max_abs_ang_vel`.
"""
max_abs_ang_vel = 1.256
"""Maximum absolute angular velocity that can be represented by the pose network. Valid for any
tangential velocity up to `max_tang_vel`.
"""


def preprocess_tang_vel(tang_vel):
    """Crops the tangential velocity to the range [0, `max_tang_vel`].

    Args:
        tang_vel: Scalar or array of tangential velocities.

    Returns:
        Scalar or array of cropped tangential velocities.
    """
    return np.min((np.max((np.zeros_like(tang_vel), tang_vel), axis=0), np.ones_like(tang_vel) * max_tang_vel), axis=0)


def preprocess_ang_vel(ang_vel):
    """Crops the angular velocity to the range [-`max_abs_ang_vel`, `max_abs_ang_vel`].

    Args:
        ang_vel: Scalar or array of angular velocities.

    Returns:
        Scalar or array of cropped angular velocities.
    """
    res = ang_vel.copy()
    if np.isscalar(res):
        if res > 0:
            res = np.min((ang_vel, np.ones_like(ang_vel) * max_abs_ang_vel), axis=0)
        elif res < 0:
            res = np.max((ang_vel, np.ones_like(ang_vel) * -max_abs_ang_vel), axis=0)
    else:
        res[ang_vel > 0] = np.min((ang_vel[ang_vel > 0], np.ones_like(ang_vel)[ang_vel > 0] * max_abs_ang_vel), axis=0)
        res[ang_vel < 0] = np.max((ang_vel[ang_vel < 0], np.ones_like(ang_vel)[ang_vel < 0] * -max_abs_ang_vel), axis=0)
    return res


def vel_to_shift_inhib(tangential_vel, angular_vel):
    """Computes shift inhibition from tangential and angular velocity using `func_to_fit3`
    parameterized by `coefs_shift_inhib`.

    Args:
        tangential_vel: Scalar tangential velocity. Will be preprocessed by `preprocess_tang_vel`.
        angular_vel: Scalar angular velocity. Will be preprocessed by `preprocess_ang_vel`.

    Returns:
        Inhibition value, lower-bounded by 0, mapped to 1 if larger than 0.0637.
    """
    shift_inhib = func_to_fit3((preprocess_tang_vel(tangential_vel), np.abs(preprocess_ang_vel(angular_vel))), *coefs_shift_inhib)
    shift_inhib = np.max((0., shift_inhib))
    if shift_inhib > 0.0637:
        shift_inhib = 1.
    return shift_inhib


def vel_to_ccw_inhib(tangential_vel, angular_vel):
    """Computes inhibition for counter-clockwise rotation from tangential and angular velocity using
    `func_to_fit3` parameterized by `coefs_rotation_inhib`.

    Args:
        tangential_vel: Scalar tangential velocity. Will be preprocessed by `preprocess_tang_vel`.
        angular_vel: Scalar angular velocity. Will be preprocessed by `preprocess_ang_vel`.

    Returns:
        Inhibition value, lower-bounded by 0, mapped to 1 if larger than 0.0656 or if the angular
        velocity is *less* than or equal to 0.
    """
    rotation_inhib = func_to_fit3((preprocess_tang_vel(tangential_vel), np.abs(preprocess_ang_vel(angular_vel))), *coefs_rotation_inhib)
    rotation_inhib = np.max((0., rotation_inhib))
    if rotation_inhib > 0.0656:
        rotation_inhib = 1.
    if angular_vel <= 0:
        rotation_inhib = 1.
    return rotation_inhib


def vel_to_cw_inhib(tangential_vel, angular_vel):
    """Computes inhibition for clockwise rotation from tangential and angular velocity using
    `func_to_fit3` parameterized by `coefs_rotation_inhib`.

    Args:
        tangential_vel: Scalar tngential velocity. Will be preprocessed by `preprocess_tang_vel`.
        angular_vel: Scalar angular velocity. Will be preprocessed by `preprocess_ang_vel`.

    Returns:
        Inhibition value, lower-bounded by 0, mapped to 1 if larger than 0.0656 or if the angular
        velocity is *greater* than or equal to 0.
    """
    rotation_inhib = func_to_fit3((preprocess_tang_vel(tangential_vel), np.abs(preprocess_ang_vel(angular_vel))), *coefs_rotation_inhib)
    rotation_inhib = np.max((0., rotation_inhib))
    if rotation_inhib > 0.0656:
        rotation_inhib = 1.
    if angular_vel >= 0:
        rotation_inhib = 1.
    return rotation_inhib


def preprocess_input_list(input) -> None:  # , time_step=0.1):
    """Brings the input command list to a standard format with at most one tangential and angular
    velocity pair per command.
    Directly modifies the input argument.

    Args:
        input: List of commands.
    """
    for super_idx in range(len(input)-1, -1, -1):
        cur_super_cmd = input[super_idx]
        idx_to_preprocess = -1
        for idx, cmd in enumerate(cur_super_cmd['cmds']):
            if cmd['cmd'] == 'velocity_array':
                idx_to_preprocess = idx
                break

        if idx_to_preprocess > -0.5:
            # duration = cur_super_cmd['duration']
            cur_cmd = cur_super_cmd['cmds'][idx_to_preprocess]
            durations = cur_cmd['durations']
            tangential_vels = cur_cmd['tangential_vels']
            angular_vels = cur_cmd['angular_vels']
            num_cmds_to_insert = len(durations)  # ceil(duration/time_step)
            cmds_to_insert = [{
                    'duration': 0.,
                    'cmds': [{'cmd': 'manual_vel',
                              'tangential_vel': 0,
                              'angular_vel': 0}]
                } for _ in range(num_cmds_to_insert)]
            # adapt duration last cmd to insert
            # cmds_to_insert[num_cmds_to_insert-1]['duration'] = round(duration - (num_cmds_to_insert-1)*time_step, 8)  # NOTE: maybe increase resolution
            for i in range(num_cmds_to_insert):
                cmds_to_insert[i]['duration'] = durations[i]
                cmds_to_insert[i]['cmds'][0]['tangential_vel'] = tangential_vels[i]
                cmds_to_insert[i]['cmds'][0]['angular_vel'] = angular_vels[i]

            del input[super_idx]

            input[super_idx:super_idx] = cmds_to_insert


def cmds_to_input_values(
    cmds: list[dict],
    fgrid_shape: GridShape,
    gauss0_f_cropped_flat: npt.NDArray[np.float64],
    encoders: npt.NDArray[np.float64],
    scale_fact: np.float64
) -> dict:
    """Converts a list of abstract commands to a single dictionary containing a more concrete input
    representation.

    For example, bump centers are combined and converted to input values for each neuron.

    Args:
        cmds: List of commands to be applied at a time step.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.
        gauss0_f_cropped_flat: Fourier coefficients of a Gaussian centered at the origin.
        encoders: Encoders of the attractor network.
        scale_fact: Scale factor that has been applied to the encoders, most likely during
        normalization.

    Raises:
        NotImplementedError: If a currently unsupported command is used.

    Returns:
        Dictionary containing near-final input for the path integration network.
    """
    # default values
    res = {
        'input': np.zeros(encoders.shape[0]),
        'shift_inhib': 1,
        'pos_rot_shift_inhib': 1,
        'neg_rot_shift_inhib': 1
    }

    for cmd in cmds:
        if cmd['cmd'] == 'input_freq':
            for bump_center in cmd['bump_centers']:
                center = get_domain() * np.array(bump_center) / np.array(fgrid_shape)
                rot_mat = get_rotation_matrix(fgrid_shape, center)
                coefs_cropped_flat = rot_mat.dot(gauss0_f_cropped_flat)
                out = coefs_cropped_flat[pose.nengo_utils.encoding_mask(fgrid_shape).ravel()]
                # out = coefs_cropped_flat
                out *= scale_fact
                out = encoders.dot(out)
                res['input'] = res['input'] + out
            res['input'][res['input'] < 0.01] -= 0.08  # inhibit other bumps
        elif cmd['cmd'] == 'manual':
            res['shift_inhib'] = cmd['shift_inhib']
            res['pos_rot_shift_inhib'] = cmd['pos_rot_shift_inhib']
            res['neg_rot_shift_inhib'] = cmd['neg_rot_shift_inhib']
        elif cmd['cmd'] == 'manual_vel':
            res['tangential_vel'] = cmd['tangential_vel']
            res['angular_vel'] = cmd['angular_vel']
        else:
            raise NotImplementedError("cmd '" + cmd['cmd'] + "' is not implemented")

    return res


# @static_inner_self
def cmd_list_to_inhib_values(
    cmds: list[dict],
    fgrid_shape: GridShape,
    gauss0_f_cropped_flat: npt.NDArray[np.float64],
    encoders: npt.NDArray[np.float64],
    scale_fact: np.float64
) -> Callable[[np.float64], dict]:
    """Returns a helper function that extracts inputs from a list of command lists given a time
    point.
    See source code for documentation of the returned function.

    Args:
        cmds: Essentially a list of command lists, where each command list is associated with a time
        point at which it is to take effect.
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.
        gauss0_f_cropped_flat: Fourier coefficients of a Gaussian centered at the origin.
        encoders: Encoders of the attractor network.
        scale_fact: Scale factor that has been applied to the encoders, most likely during
        normalization.

    Returns:
        ``cmd_list_to_input_values``.
    """
    cmd_idx = 0
    t_up_to_cur_cmd = 0

    def cmd_list_to_input_values(t):
        """Wrapper for ``cmds_to_input_values`` that returns input values for a specified time
        point based on a list of command lists.

        The function keeps track of the time point for which it has been called last, and advances
        the list of command lists as necessary.

        Args:
            t: Time point in seconds.

        Raises:
            RuntimeError: If called with a time parameter that exceeds the covered time range.

        Returns:
            Dictionary containing near-final input for the path integration network.
        """
        nonlocal cmd_idx, t_up_to_cur_cmd

        if (t_up_to_cur_cmd + cmds[cmd_idx]['duration']) > t:
            pass
        elif len(cmds) > (cmd_idx + 1):
            t_up_to_cur_cmd = t_up_to_cur_cmd + cmds[cmd_idx]['duration']
            cmd_idx = cmd_idx + 1
        else:
            raise RuntimeError('out of inhib commands (t=' + str(t) + ')')

        return cmds_to_input_values(cmds[cmd_idx]['cmds'], fgrid_shape, gauss0_f_cropped_flat, encoders, scale_fact)

    return cmd_list_to_input_values


def get_circ_traj(radius, radian_per_second, center=np.zeros(2), phase_shift=0.0):
    """Generate waypoints of circular trajectory with given radius."""
    def circ_traj(t):
        """t can be scalar or ndarray; returns sequence of waypoints"""

        arg = t*radian_per_second
        vec = np.stack((np.cos(phase_shift+arg), np.sin(phase_shift+arg)), axis=-1)
        return radius * vec + center

    return circ_traj


def traj_to_inhib(
    waypoints: npt.NDArray[np.float64],
    initial_orientation: np.float64 = 0.0,
    dt: np.float64 = 1.0
) -> npt.NDArray[np.float64]:
    """Convert an array of waypoints to an array of modulation values.

    Args:
        waypoints: Positions ``(x,y)`` at each time step. Shape ``(T,2)``, where ``T`` is the number
                   of time steps.
        initial_orientation: Heading angle at ``t=0``. Defaults to 0.0.
        dt: Time in seconds in which the next position needs to be reached. Defaults to 1.0.

    Returns:
        Modulation values for the shift and rotation inhibition nodes. Shape ``(T,3)``.
    """
    cur = waypoints[0]
    cur_orientation = initial_orientation
    mod_vals_arr = np.zeros((waypoints.shape[0]-1, 3))

    for t in range(1, waypoints.shape[0]):
        delta = waypoints[t] - cur
        mod_vals_arr[t-1] = delta_to_inhib(delta, cur_orientation, dt)
        cur = waypoints[t]
        # assume that the orientation after the current step corresponds to the angle of the displacement vector of the current step
        cur_orientation = np.arctan2(delta[1], delta[0])

    return mod_vals_arr


def delta_to_inhib(
    delta: npt.NDArray[np.float64],
    initial_orientation: np.float64,
    dt: np.float64 = 1.0
):
    """Convert a combination of space delta and dt to an array of modulation values.

    Args:
        delta: Vector from the current position to the target position. Shape ``(2,)``.
        initial_orientation: Heading angle in radians before applying delta.
        dt: Time in seconds in which the next position needs to be reached. Defaults to 1.0.

    Returns:
        Modulation values for the shift inhibition node, and two the rotation inhibition nodes.
        Shape ``(3,)``.
    """
    tangential_factor = 6.26780626781  # 1#0.5698005698005698
    angular_factor = 1.85185185185  # 1#0.3703703703703704
    # m/s  # 0.5  https://www.frontiersin.org/articles/10.3389/fphys.2018.00042/full (Table 2)
    max_tangential_velocity = 2.0  # TODO: determine true max
    max_angular_velocity = pi  # rad/s  TODO: determine true max

    mod_vals = np.zeros(3)
    tangential_delta = np.linalg.norm(delta)
    tangential_velocity = tangential_delta / dt
    if tangential_velocity > max_tangential_velocity:
        tangential_velocity = max_tangential_velocity
    mod_vals[0] = 1 - tangential_factor * tangential_velocity

    tmp = np.arctan2(delta[1], delta[0])
    angular_delta = tmp - initial_orientation
    _, angular_delta = np.divmod(angular_delta, 2*pi)
    if angular_delta <= pi:
        # print('pos')
        angular_velocity = angular_delta / dt
        if angular_velocity > max_angular_velocity:
            angular_velocity = max_angular_velocity
        mod_vals[1] = 1 - angular_factor * angular_velocity
    else:
        # print('neg')
        angular_delta = 2*pi - angular_delta
        angular_velocity = angular_delta / dt
        if angular_velocity > max_angular_velocity:
            angular_velocity = max_angular_velocity
        mod_vals[2] = 1 - angular_factor * angular_velocity

    return mod_vals

# expects array of tangential and angular velocities at each time step
# def traj_to_inhib(tan_vel, ang_vel):
#     fact_tangential = 1
#     fact_angular = 1


def delta_to_velocities(
    delta: npt.NDArray[np.float64],
    initial_orientation: np.float64,
    dt: np.float64 = 1.0
):
    """Convert a combination of space delta and dt to an array of tangential and angular velocities.

    Args:
        delta: Vector from the current position to the target position. Shape ``(2,)``.
        initial_orientation: Heading angle in radians before applying delta.
        dt: Time in seconds in which the next position needs to be reached. Defaults to 1.0.

    Returns:
        Tangential and angular velocities. Shape ``(2,)``.
    """
    velocities = np.zeros(2)
    tangential_delta = np.linalg.norm(delta)
    tangential_velocity = tangential_delta / dt
    velocities[0] = tangential_velocity

    tmp = np.arctan2(delta[1], delta[0])
    angular_delta = tmp - initial_orientation
    _, angular_delta = np.divmod(angular_delta, 2*pi)
    if angular_delta > pi:
        # print('neg')
        angular_delta = -(2*pi - angular_delta)
    angular_velocity = angular_delta / dt
    velocities[1] = angular_velocity

    return velocities


def traj_to_velocities(
    waypoints: npt.NDArray[np.float64],
    dt: npt.NDArray[np.float64],
    initial_orientation: np.float64 = 0.0
) -> npt.NDArray[np.float64]:
    """Converts an array of waypoints to an array of tangential and angular velocities.

    Args:
        waypoints: Positions ``(x,y)`` at each time step. Shape ``(T,2)``, where ``T`` is the number
                   of time steps.
        initial_orientation: Heading angle at ``t=0``. Defaults to 0.0.
        dt: Time in seconds in which the next position needs to be reached. Defaults to 1.0.

    Returns:
        Array of tangential and angular values. Shape ``(T,2)``.
    """
    cur = waypoints[0]
    cur_orientation = initial_orientation
    vel_arr = np.zeros((waypoints.shape[0]-1, 2))

    for t in range(1, waypoints.shape[0]):
        delta = waypoints[t] - cur
        vel_arr[t-1] = delta_to_velocities(delta, cur_orientation, dt[t])
        cur = waypoints[t]
        # assume that the orientation after the current step corresponds to the angle of the displacement vector of the current step
        cur_orientation = np.arctan2(delta[1], delta[0])

    return vel_arr


def velocities_to_traj(
    tang_vels,
    ang_vels,
    starting_point,
    initial_orientation,
    dt
):
    """Converts an array of tangential and angular velocities to an array of waypoints.
    Essentially integrates the change caused by the instantaneous velocities over time.

    Args:
        tang_vels: Array of tangential velocities, one value for each time step.
        ang_vels: Array of angular velocities, one value for each time step.
        starting_point: ``(x,y)`` position at ``t=0``.
        initial_orientation: Heading angle at ``t=0``.
        dt: Time in seconds between two consecutive data points. Can be an array or scalar.

    Returns:
        Array of waypoints.
    """
    if np.isscalar(dt):
        dt = dt * np.ones(tang_vels.shape[0])

    traj = np.zeros((tang_vels.shape[0]+1, 3))
    cur_pos = starting_point
    traj[0, :2] = cur_pos
    cur_angle = initial_orientation
    traj[0, 2] = cur_angle
    for t in range(tang_vels.shape[0]):
        cur_heading_vector = np.array([np.cos(cur_angle), np.sin(cur_angle)])
        cur_pos = cur_pos + cur_heading_vector * tang_vels[t] * dt[t]
        traj[t+1, :2] = cur_pos
        cur_angle += ang_vels[t] * dt[t]
        traj[t+1, 2] = cur_angle

    return traj
