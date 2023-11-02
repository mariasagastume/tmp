"""
Construct and work with the unit domain (rhombic prism), hexagonal grids and corresponding distance
matrices. Provides functionality to wrap poses into the rhombic area or conceptually unroll it, as
well as to convert between representations with rectangular and rhombic bases.
"""
import logging
from math import sqrt
import numpy as np
import numpy.typing as npt

from pose.typing import GridShape


logger = logging.getLogger(__name__)


fspace_base = np.array([[1, 0.5, 0], [0, sqrt(3)/2, 0], [0, 0, 1]])
"""Basis vectors of the reciprocal space or, equivalently, transformation matrix from reciprocal
space to real space.
"""

inv_fspace_base = np.array([[1, -0.577350269189626, 0], [0, 2/sqrt(3), 0], [0, 0, 1]])
"""Basis vectors of the real space in reciprocal space or, equivalently, transformation matrix from
real space to reciprocal space.
"""


def get_domain() -> npt.NDArray[np.float64]:
    """Provide the domain of the unit cell of the hexagonal Bravais lattice.

    Returns:
        Domain extent in all dimensions. Shape ``(3,)``.
    """
    return np.array([1.0, sqrt(3)/2, 1.0])


def polar_to_cartesian(
    r: float,
    theta: float
) -> npt.NDArray[np.float64]:
    """Convert polar coordinates in the x-y plane to three-dimensional Cartesian coordinates.

    Args:
        r: Radius.
        theta: Angle in radian.

    Returns:
        Cartesian coordinates with z-component of 0.
    """
    vec = r * np.exp(1j * theta)
    x, y = vec.real, vec.imag
    return np.array([x, y, 0])


def get_3d_coordinates(
    grid_shape: GridShape
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Computes the coordinates of lattice points in the unit cell wrapped into a rectangular
    cuboid.

    Args:
        grid_shape: Shape of the lattice of the unit cell.

    Returns:
        Coordinate arrays for each dimension, which contain points in their order of appearance in
        the rectangular cuboid.
    """
    grid_shape = np.array(grid_shape)
    sheet_dimensions = get_domain()

    start_vals = np.zeros(3)
    end_vals = sheet_dimensions - sheet_dimensions/grid_shape
    res_cmplx = grid_shape * 1j

    u, v, w = np.mgrid[start_vals[0]:end_vals[0]:res_cmplx[0],
                       start_vals[1]:end_vals[1]:res_cmplx[1],
                       start_vals[2]:end_vals[2]:res_cmplx[2]]

    # hardcoded factor depends on generators
    u[:, 1::2, :] += sheet_dimensions[0]/grid_shape[0] * 0.5

    return u, v, w


def get_2d_distances(
    grid_shape: GridShape
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Computes the signed pairwise distances between all points in the unit cell of a
    two-dimensional hexagonal Bravais lattice, wrapped into a rectangle. Parts adapted from https://github.com/DiogoSantosPata/gridcells.

    Args:
        grid_shape: Shape of the unit cell of a compatible three-dimensional lattice.

    Returns:
        A tuple ``(u_diff, v_diff)``, where ``u_diff`` contains the signed pairwise distances
        between lattice points in x-dimension (``u_diff[i,j]`` points from point ``i`` to
        point ``j`` (projected onto x)), and ``v_diff`` contains the analogous information for the
        y-dimension.

    Notes:
        ``np.sqrt(u_diff**2 + v_diff**2)`` gives the pairwise absolute distances between points.
    """
    u, v, _ = get_3d_coordinates(grid_shape)

    twist_correction_x = np.array([0, -0.5, -0.5, 0.5, 0.5, -1, 1])
    twist_correction_y = np.array([0, np.sqrt(3)/2, -np.sqrt(3)/2, np.sqrt(3)/2, -np.sqrt(3)/2, 0, 0])

    u_xx, u_yy = np.meshgrid(np.ravel(u[:, :, 0]), np.ravel(u[:, :, 0]))
    v_xx, v_yy = np.meshgrid(np.ravel(v[:, :, 0]), np.ravel(v[:, :, 0]))

    u_diff = u_xx - u_yy
    v_diff = v_xx - v_yy

    for ii in range(len(twist_correction_x)):
        aaa1 = np.sqrt(u_diff**2 + v_diff**2)
        u_rrr = u_xx - u_yy + twist_correction_x[ii]
        v_rrr = v_xx - v_yy + twist_correction_y[ii]
        aaa2 = np.sqrt(u_rrr**2 + v_rrr**2)
        iii = np.where(aaa2 < aaa1)
        u_diff[iii] = u_rrr[iii]
        v_diff[iii] = v_rrr[iii]

    return u_diff, v_diff


def get_3d_distances(
    grid_shape: GridShape
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Computes the signed pairwise distances between all points in the unit cell of a
    three-dimensional hexagonal Bravais lattice, wrapped into a rectangular cuboid.

    Args:
        grid_shape: Shape of the unit cell of the lattice.

    Returns:
        A tuple ``(u_diff, v_diff, w_diff)``, where ``u_diff`` contains the signed pairwise
        distances between lattice points in x-dimension (``u_diff[i,j]`` points from point ``i`` to
        point ``j`` (projected onto x)), ``v_diff`` and ``w_diff`` contain the analogous information
        for the y- and z-axis, respectively.
    """
    _, _, w = get_3d_coordinates(grid_shape)

    u_diff, v_diff = get_2d_distances(grid_shape)
    zres = grid_shape[2]
    u_diff_expanded = np.repeat(u_diff, repeats=zres, axis=1)
    u_diff_expanded = np.repeat(u_diff_expanded, repeats=zres, axis=0)
    v_diff_expanded = np.repeat(v_diff, repeats=zres, axis=1)
    v_diff_expanded = np.repeat(v_diff_expanded, repeats=zres, axis=0)

    twist_correction_z = np.array([0, 1, -1])

    w_xx, w_yy = np.meshgrid(np.ravel(w), np.ravel(w))

    # w_diff[0] contains the distances from all neurons in layer 0 to all other neurons ordering is
    # row-major, meaning y- changes faster than x-coordinate
    w_diff = w_xx - w_yy

    for ii in range(len(twist_correction_z)):
        # could potentially only consider w_diff since this dimension is independent of u and v
        aaa1 = np.sqrt(u_diff_expanded**2 + v_diff_expanded**2 + w_diff**2)
        w_rrr = w_xx - w_yy + twist_correction_z[ii]
        aaa2 = np.sqrt(u_diff_expanded**2 + v_diff_expanded**2 + w_rrr**2)
        iii = np.where(aaa2 < aaa1)
        w_diff[iii] = w_rrr[iii]

    # TODO: verify that no transpose required
    return u_diff_expanded, v_diff_expanded, w_diff


def get_3d_distances_unwrapped(
    grid_shape: GridShape
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Computes the signed pairwise distances between all points in the unit cell of a
    three-dimensional hexagonal Bravais lattice.

    Args:
        grid_shape: Shape of the unit cell of the lattice.

    Returns:
        A tuple ``(u_diff, v_diff, w_diff)``, where ``u_diff`` contains the signed pairwise
        distances between lattice points in x-dimension (``u_diff[i,j]`` points from point ``i`` to
        point ``j`` (projected onto x)), ``v_diff`` and ``w_diff`` contain the analogous information
        for the y- and z-axis, respectively.
    """
    u_diff, v_diff, w_diff = get_3d_distances(grid_shape)
    u_diff_unwrapped = unwrap_multi(
        u_diff.reshape((*grid_shape, *grid_shape)), grid_shape, 1).reshape((np.prod(grid_shape), np.prod(grid_shape)))
    v_diff_unwrapped = unwrap_multi(
        v_diff.reshape((*grid_shape, *grid_shape)), grid_shape, 1).reshape((np.prod(grid_shape), np.prod(grid_shape)))
    w_diff_unwrapped = unwrap_multi(
        w_diff.reshape((*grid_shape, *grid_shape)), grid_shape, 1).reshape((np.prod(grid_shape), np.prod(grid_shape)))

    return u_diff_unwrapped, v_diff_unwrapped, w_diff_unwrapped


def unwrap_single(
    wrapped_data: npt.NDArray[np.float64],
    grid_shape: GridShape,
    dim: np.float64
) -> npt.NDArray[np.float64]:
    """Unwraps data from the wrapped unit cell to the regular unit cell.

    If ``dim > 1``, assumes that the individual data points correspond to coordinates on the lattice
    (``dim = 3``) and corrects the z-dimension of these coordinates accordingly.

    Args:
        wrapped_data: Data corresponding to and arranged like points in the wrapped unit cell.
        grid_shape: Shape of the unit cell of the lattice.
        dim: Dimension of a single data point.

    Returns:
        Data corresponding to points in the regular unit cell.
    """
    if dim == 1:
        res = np.zeros(grid_shape)
    else:
        res = np.zeros((*grid_shape, dim))

    for u in range(grid_shape[0]):
        for v in range(grid_shape[1]):
            u_corrected = u
            if v > 1:
                u_corrected = (u+(v//2)) % grid_shape[0]
            res[u, v, :] = wrapped_data[u_corrected, v, :]
            if v > 1 and dim > 1 and (u+(v//2)) >= grid_shape[0]:
                res[u, v, :, 0] = res[u, v, :, 0] + 1

    return res


def unwrap_multi(
    wrapped_data: npt.NDArray[np.float64],
    grid_shape: GridShape,
    dim: np.float64
) -> npt.NDArray[np.float64]:
    """Unwraps data specified for each point in the wrapped unit cell, where for each point the data
    amounts in turn to a data point for all points in the wrapped unit cell, to the regular unit
    cell (on two levels).

    If ``dim > 1``, assumes that the individual data points correspond to coordinates on the lattice
    (``dim = 3``) and corrects the z-dimension of these coordinates accordingly.

    Uses ``unwrap_single``.

    Args:
        wrapped_data: Data corresponding to and arranged like points in the wrapped unit cell, on
                      two levels.
        grid_shape: Shape of the unit cell of the lattice.
        dim: Dimension of a single data point.

    Returns:
        Data corresponding to points in the regular unit cell, on two levels.
    """
    if dim == 1:
        res = np.zeros((*grid_shape, *grid_shape))
    else:
        res = np.zeros((*grid_shape, *grid_shape, dim))

    for u in range(grid_shape[0]):
        for v in range(grid_shape[1]):
            for w in range(grid_shape[2]):
                u_corrected = u
                if v > 1:
                    u_corrected = (u+(v//2)) % grid_shape[0]
                res[u, v, w] = unwrap_single(wrapped_data[u_corrected, v, w], grid_shape, dim)

    return res


def get_3d_coordinates_unwrapped(
    grid_shape: GridShape,
    generators: npt.NDArray[np.float64]
) -> npt.NDArray[np.float64]:
    """Computes the coordinates of lattice points in the unit cell of a three-dimensional hexagonal
    Bravais lattice.

    Args:
        grid_shape: Shape of a unit cell of the neuron lattice.
        generators: Primitive translation vectors of the primitive unit cell of the lattice.

    Returns:
        Array of coordinates.
    """
    res = np.zeros((*grid_shape, 3))

    # TODO: vectorize
    for u in range(grid_shape[0]):
        for v in range(grid_shape[1]):
            for w in range(grid_shape[2]):
                res[u, v, w] = generators.dot(np.array([u, v, w]))

    return res


def get_3d_coordinates_unwrapped_vectorized(
    grid_shape: GridShape,
    generators: npt.NDArray[np.float64]
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Wrapper of ``get_3d_coordinates_unwrapped`` that returns coordinate arrays in vectorized
    format.

    Args:
        grid_shape: Shape of a unit cell of the neuron lattice.
        generators: Primitive translation vectors of the primitive unit cell of the lattice.

    Returns:
        Coordinate arrays for each dimension.
    """
    un_vectorized = get_3d_coordinates_unwrapped(grid_shape, generators)

    XXX = un_vectorized[:, :, :, 0]
    YYY = un_vectorized[:, :, :, 1]
    ZZZ = un_vectorized[:, :, :, 2]

    return XXX, YYY, ZZZ


def wrap_closer(
    ref_point: npt.NDArray[np.float64],
    points: npt.NDArray[np.float64]
) -> npt.NDArray[np.float64]:
    """Wraps points as close as possible to a reference point.

    Args:
        ref_point: Reference point in reciprocal space to which the points should be wrapped close.
        points: Points to wrap in reciprocal space.

    Returns:
        Array of wrapped points in reciprocal space.
    """
    indiv_offsets = np.arange(-5, 6).tolist()
    offsets = np.stack(np.meshgrid(indiv_offsets, indiv_offsets, indiv_offsets), -1).reshape(-1, 3)
    points_modified = np.repeat(points, offsets.shape[0], axis=0).reshape((points.shape[0], offsets.shape[0], -1))
    point1_offsets = points_modified + offsets
    point1_offsets_minus_ref_point = point1_offsets - ref_point
    # even if this were not entirely correct, it would give correct results for our purpose
    point1_offsets_minus_ref_point_distances = np.linalg.norm(point1_offsets_minus_ref_point, axis=2)
    best_offset = np.argmin(point1_offsets_minus_ref_point_distances, axis=1)
    wrapped_points = point1_offsets[np.arange(points.shape[0]), best_offset]

    return wrapped_points


def wrap_into_parallelogram(
    points: npt.NDArray[np.float64]
) -> npt.NDArray[np.float64]:
    """Wraps points into the unit cell of a three-dimensional hexagonal Bravais lattice.

    Assumes all values are in the range -1 to 2.

    Args:
        points: Points to wrap in reciprocal space.

    Returns:
        Wrapped points in reciprocal space.
    """
    points[points < 0] += 1
    points[points > 1] -= 1

    # return a view, not a copy; can be ignored by caller
    return points[...]
