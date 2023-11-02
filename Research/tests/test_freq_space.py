import numpy as np
import unittest

from pose.freq_space import (
    get_domain,
    get_rotation_matrix,
    get_fftn_freqs,
    get_0_coefs
)


class TestFreqSpace(unittest.TestCase):
    def test_get_rotation_matrix(self):
        fgrid_shape = (4, 4, 4)
        for index in np.ndindex(fgrid_shape):
            center = get_domain() * np.array(index) / np.array(fgrid_shape)
            rot_mat = get_rotation_matrix(fgrid_shape, center)
            self.assertAlmostEqual(np.linalg.det(rot_mat), 1)

        center1 = get_domain() * np.array([2, 3, 3]) / np.array(fgrid_shape)
        rot_mat1 = get_rotation_matrix(fgrid_shape, center1)
        center2 = get_domain() * np.array([2, 7, 3]) / np.array(fgrid_shape)
        rot_mat2 = get_rotation_matrix(fgrid_shape, center2)
        np.testing.assert_allclose(rot_mat1, rot_mat2, atol=1e-10)

    def test_get_fftn_freqs(self):
        fgrid_shape = (7, 7, 7)
        freqs_x, freqs_y, freqs_z = get_fftn_freqs(fgrid_shape)
        np.testing.assert_allclose(
            freqs_x,
            np.array([0., 1., 2., 3., -3., -2., -1.]),
            rtol=1e-8)
        np.testing.assert_allclose(
            freqs_y,
            np.array([0., 1.15470054, 2.30940108, 3.46410162, -3.46410162, -2.30940108, -1.15470054]),
            rtol=1e-8)
        np.testing.assert_allclose(
            freqs_z,
            np.array([0., 1., 2., 3., -3., -2., -1.]),
            rtol=1e-8)

        freqs_x, freqs_y, freqs_z = get_fftn_freqs((8, 8, 8))
        np.testing.assert_allclose(
            freqs_x,
            np.array([0., 1., 2., 3., -4., -3., -2., -1.]),
            rtol=1e-8)
        np.testing.assert_allclose(
            freqs_y,
            np.array([0., 1.15470054, 2.30940108, 3.46410162, -4.61880215,  -3.46410162, -2.30940108, -1.15470054]),
            rtol=1e-8)
        np.testing.assert_allclose(
            freqs_z,
            np.array([0., 1., 2., 3., -4., -3., -2., -1.]),
            rtol=1e-8)

        freqs_x, freqs_y, freqs_z = get_fftn_freqs((7, 8, 9))
        np.testing.assert_allclose(
            freqs_x,
            np.array([0., 1., 2., 3., -3., -2., -1.]),
            rtol=1e-8)
        np.testing.assert_allclose(
            freqs_y,
            np.array([0., 1.15470054, 2.30940108, 3.46410162, -4.61880215, -3.46410162, -2.30940108, -1.15470054]),
            rtol=1e-8)
        np.testing.assert_allclose(
            freqs_z,
            np.array([0., 1., 2., 3., 4., -4., -3., -2., -1.]),
            rtol=1e-8)

        freqs_x, freqs_y, freqs_z = get_fftn_freqs((8, 9, 10))
        np.testing.assert_allclose(
            freqs_x,
            np.array([0., 1., 2., 3., -4., -3., -2., -1.]),
            rtol=1e-8)
        np.testing.assert_allclose(
            freqs_y,
            np.array([0., 1.15470054, 2.30940108, 3.46410162, 4.61880215,
                     -4.61880215, -3.46410162, -2.30940108, -1.15470054]),
            rtol=1e-8)
        np.testing.assert_allclose(
            freqs_z,
            np.array([0., 1., 2., 3., 4., -5., -4., -3., -2., -1.]),
            rtol=1e-8)

    def test_get_0_coefs(self):
        fgrid_shape = (4, 4, 4)
        cov = np.eye(3) * 0.05
        zero_coefs = get_0_coefs(fgrid_shape, cov)
        np.testing.assert_allclose(
            zero_coefs,
            np.array([8.89626686e-01,  0.00000000e+00,  3.79354595e-01,  0.00000000e+00,
                      4.77838528e-03,  0.00000000e+00,  3.79354595e-01,  0.00000000e+00,
                      2.78193197e-01,  8.11249883e-17,  1.18627138e-01,  4.80740672e-17,
                      1.49423831e-03,  3.00462920e-18,  1.18627138e-01,  4.80740672e-17,
                      -2.16664842e-02,  0.00000000e+00, -9.23902177e-03,  0.00000000e+00,
                      -1.16375566e-04,  0.00000000e+00, -9.23902177e-03,  0.00000000e+00,
                      2.78193197e-01, -8.11249883e-17,  1.18627138e-01, -4.80740672e-17,
                      1.49423831e-03, -3.00462920e-18,  1.18627138e-01, -4.80740672e-17,
                      2.78193197e-01, -9.61481343e-17,  1.18627138e-01, -2.40370336e-17,
                      1.49423831e-03,  1.50231460e-18,  1.18627138e-01, -2.40370336e-17,
                      2.78193197e-01,  7.51157299e-17,  1.18627138e-01,  2.70416628e-17,
                      1.49423831e-03, -1.50231460e-18,  1.18627138e-01,  2.70416628e-17,
                      2.54917273e-02, -2.40370336e-17,  1.08701819e-02,  0.00000000e+00,
                      1.36921809e-04, -1.50231460e-18,  1.08701819e-02,  0.00000000e+00,
                      2.54917273e-02,  2.10324044e-17,  1.08701819e-02,  3.00462920e-18,
                      1.36921809e-04,  1.50231460e-18,  1.08701819e-02,  3.00462920e-18,
                      -2.16664842e-02,  0.00000000e+00, -9.23902177e-03,  0.00000000e+00,
                      -1.16375566e-04,  0.00000000e+00, -9.23902177e-03,  0.00000000e+00,
                      2.54917273e-02,  9.01388759e-18,  1.08701819e-02,  0.00000000e+00,
                      1.36921809e-04,  0.00000000e+00,  1.08701819e-02,  0.00000000e+00,
                      -2.16664842e-02,  0.00000000e+00, -9.23902177e-03,  0.00000000e+00,
                      -1.16375566e-04,  0.00000000e+00, -9.23902177e-03,  0.00000000e+00,
                      2.54917273e-02, -9.01388759e-18,  1.08701819e-02,  0.00000000e+00,
                      1.36921809e-04,  0.00000000e+00,  1.08701819e-02,  0.00000000e+00,
                      2.78193197e-01,  9.61481343e-17,  1.18627138e-01,  2.40370336e-17,
                      1.49423831e-03, -1.50231460e-18,  1.18627138e-01,  2.40370336e-17,
                      2.54917273e-02, -2.10324044e-17,  1.08701819e-02, -3.00462920e-18,
                      1.36921809e-04, -1.50231460e-18,  1.08701819e-02, -3.00462920e-18,
                      2.54917273e-02,  2.40370336e-17,  1.08701819e-02,  0.00000000e+00,
                      1.36921809e-04,  1.50231460e-18,  1.08701819e-02,  0.00000000e+00,
                      2.78193197e-01, -7.51157299e-17,  1.18627138e-01, -2.70416628e-17,
                      1.49423831e-03,  1.50231460e-18,  1.18627138e-01, -2.70416628e-17]),
            rtol=1e-8)


if __name__ == '__main__':
    unittest.main()
