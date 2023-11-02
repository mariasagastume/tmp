"""
Construct and manipulate representations in reciprocal space.
"""
import logging
import numpy as np
from numpy.fft import fftfreq
from scipy.stats import multivariate_normal
import numpy.typing as npt

from pose.hex import (
    get_domain,
    get_3d_distances,
    unwrap_single
)
from pose.typing import GridShape


logger = logging.getLogger(__name__)


def get_fftn_freqs(
    fgrid_shape: GridShape
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Compute the frequency bin centers in cycles per unit of the sample spacing.

    Args:
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        Frequencies associated with the individual Fourier coefficients.
    """
    num_samples = np.array(fgrid_shape)  # make sure that we work with an array
    window_length = get_domain()
    sample_spacing = window_length / num_samples

    freqs_x = fftfreq(num_samples[0], sample_spacing[0])
    freqs_y = fftfreq(num_samples[1], sample_spacing[1])
    freqs_z = fftfreq(num_samples[2], sample_spacing[2])

    return freqs_x, freqs_y, freqs_z


def get_rotation_matrix(
    fgrid_shape: GridShape,
    shift: npt.ArrayLike
) -> npt.NDArray[np.float64]:
    """Computes a rotation matrix for a x,y,z-rotation in reciprocal space.

    The vectors to be rotated are expected in flattened complex space (see ``flatten_coefs``).

    For example, we can shift the center of the Gaussian around by applying such a rotation matrix
    to the coefficients.

    Args:
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.
        shift: Shift vector in reciprocal space.

    Returns:
        A square rotation matrix ``R``, satisfying ``R.T = inv(R)``.
    """
    # if crop_conj_sym:
    #     n_coef = _rncoef_flat(fourier_coef_shape)
    #     freqs_x, freqs_y, freqs_z = _rfftn_freqs(fourier_coef_shape)
    #     rfcshape = _rfcshape(fourier_coef_shape)
    n_coef = np.prod(fgrid_shape) * 2
    freqs_x, freqs_y, freqs_z = get_fftn_freqs(fgrid_shape)

    rot_mat = np.zeros((n_coef, n_coef))

    i = 0
    for idx_x in range(fgrid_shape[0]):
        for idx_y in range(fgrid_shape[1]):
            for idx_z in range(fgrid_shape[2]):
                freq_x = freqs_x[idx_x]
                freq_y = freqs_y[idx_y]
                freq_z = freqs_z[idx_z]

                eval_point = 2*np.pi*freq_x*shift[0] + 2*np.pi*freq_y*shift[1] + 2*np.pi*freq_z*shift[2]

                rot_mat[i, i] = np.cos(eval_point)
                rot_mat[i, i+1] = np.sin(eval_point)

                # zero imaginary part at Nyquist locations
                # if (idx_x == 0 or (fourier_coef_shape[0] % 2 == 0 and idx_x == fourier_coef_shape[0]//2)) and (idx_y == 0 or (fourier_coef_shape[1] % 2 == 0 and idx_y == fourier_coef_shape[1]//2)) and (idx_z == 0 or (fourier_coef_shape[2] % 2 == 0 and idx_z == fourier_coef_shape[2]//2)):
                #     rot_mat[i+1, i] = 0
                #     rot_mat[i+1, i+1] = 0
                # else:
                #     rot_mat[i+1, i] = -np.sin(eval_point)
                #     rot_mat[i+1, i+1] = np.cos(eval_point)

                rot_mat[i+1, i] = -np.sin(eval_point)
                rot_mat[i+1, i+1] = np.cos(eval_point)

                i += 2

    return rot_mat


def flatten_coefs(
    coefs: npt.NDArray[np.complex128]
) -> npt.NDArray[np.float64]:
    """Transforms Fourier coefficients into flattened complex space, i.e. flattened dimensions and
    interleaved real and imaginary parts.

    Args:
        coefs: Fourier coefficients.

    Returns:
        Interleaved real and imaginary parts of Fourier coefficients. Shape ``(coefs.size*2,)``.
    """
    coefs_flat = coefs.flatten()
    res = np.zeros(len(coefs_flat)*2, dtype=np.float64)
    res[0::2] = np.real(coefs_flat)
    res[1::2] = np.imag(coefs_flat)
    return res


def unflatten_coefs(
    coefs: npt.NDArray[np.float64],
    fgrid_shape: GridShape = None
) -> npt.NDArray[np.complex128]:
    """Transforms Fourier coefficients from flattened complex space (see ``flatten_coefs``) into
    complex space.

    Args:
        coefs: Fourier coefficients in flattened complex space.
        fgrid_shape: Desired final shape of the returned array. Defaults to None.

    Returns:
        Fourier coefficients.
    """
    res_flat = np.zeros(len(coefs)//2, dtype=np.complex128)
    res_flat = coefs[0::2]
    res_flat = res_flat + coefs[1::2] * 1.0j
    res = res_flat
    if fgrid_shape is not None:
        res = res.reshape(fgrid_shape)
    return res


# keep just the real parts of nyquist terms
def get_nyquist_mask(
    fgrid_shape: GridShape
) -> npt.NDArray[np.bool_]:
    """
    Computes an index mask to omit the imaginary part of Fourier coefficients where the index along
    any axes is 0 or the index is half of the axis-length. For dimensions of even length these
    correspond to the Nyquist terms.

    Args:
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.

    Returns:
        Index mask. Shape ``(np.prod(fgrid_shape)*2,)``.
    """
    mask = np.ones(fgrid_shape, dtype=bool)
    mask2 = mask.flatten()

    for idx_x in range(fgrid_shape[0]):
        for idx_y in range(fgrid_shape[1]):
            for idx_z in range(fgrid_shape[2]):
                if (idx_x == 0 or (fgrid_shape[0] % 2 == 0 and idx_x == fgrid_shape[0]//2)) and (idx_y == 0 or (fgrid_shape[1] % 2 == 0 and idx_y == fgrid_shape[1]//2)) and (idx_z == 0 or (fgrid_shape[2] % 2 == 0 and idx_z == fgrid_shape[2]//2)):
                    mask[idx_x, idx_y, idx_z] = 0

    mask = mask.flatten()
    mask_flat = np.stack((mask2, mask), 1).flatten()  # duplicate mask since separate real and imag parts

    return mask_flat


def fftn_hex(
    data: npt.NDArray[np.float64]
) -> npt.NDArray[np.complex128]:
    """Compute the multidimensional FFT on the hexagonal lattice.

    In particular, account for the reduced domain of ``sqrt(3)/2`` along the y-axis.

    Args:
        data: Sampled volume data in real space.

    Returns:
        Fourier coefficients.

    Notes:
        The regular FFT assumes orthogonal axes. We have to account for the relative deviation
        from a $\mathbb{Z}^3$ grid. This amounts to a multiplication by the product of the domain
        extents in all dimensions. In particular, the rectified input to the FFT has an extent of
        ``sqrt(3)/2`` in the y-dimension and, therefore, we effectively multiply the regular FFT
        output by this value.
    """
    # reflects the relative deviation of the grid from a Z**3 grid OR the domain size (product); the 'regular' fft assumes orthogonal axes
    return np.fft.fftn(data, norm='forward') * np.prod(get_domain())


def ifftn_hex(
    data: npt.NDArray[np.complex128]
) -> npt.NDArray[np.float64]:
    """Compute the multidimensional inverse FFT on the reciprocal hexagonal lattice.

    Args:
        data: Fourier coefficients.

    Returns:
        Volume data in real space.
    """
    res = np.fft.ifftn(data, norm='forward') / np.prod(get_domain())
    res = np.real(res)

    return res


def get_0_coefs(
    fgrid_shape: GridShape,
    cov: npt.NDArray[np.float64]
) -> npt.NDArray[np.float64]:
    """Compute the Fourier coefficients of a three-dimensional Gaussian bump centered at the origin
    and sampled on the unit cell.

    Args:
        fgrid_shape: Shape of the discrete sampling grid for the FFT, and of the reciprocal grid.
        cov: Covariance matrix.

    Returns:
        Flattened Fourier coefficients.
    """
    # bf = BumpFunction(np.zeros(3), cov, generators, fourier_coef_shape)
    # coefs = bf.get_values_dual_unshuffled().reshape(fourier_coef_shape)
    # coefs_cropped = crop_conjugate_symmetry(coefs, fourier_coef_shape)
    # coefs_flat = flatten_coefs(coefs_cropped)
    # # coefs_final = np.delete(coefs_flat, 1, 0)

    u_diff, v_diff, w_diff = get_3d_distances(fgrid_shape)
    pos = np.stack((u_diff[0], v_diff[0], w_diff[0]), axis=-1)
    Z = multivariate_normal.pdf(x=pos, mean=np.zeros(3), cov=cov).reshape(fgrid_shape)
    Z = unwrap_single(Z, fgrid_shape, 1)  # confirmed correct with MATLAB
    zero_coefs = fftn_hex(Z)
    coefs_flat = flatten_coefs(zero_coefs)

    return coefs_flat
