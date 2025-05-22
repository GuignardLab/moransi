from .._moransi import morans_i_image, morans_i_adjacency_matrix
from scipy.ndimage import generate_binary_structure
from libpysal.weights import lat2W
import numpy as np

np.random.seed(0)
im_rand = np.random.random((99, 99))

im_check = (np.arange(99 * 99) % 2 - 1).reshape(99, -1)

im_half = (np.arange(99 * 99) < 99 * 99 / 2 - 1).reshape(99, -1)


def get_adj_metric(im):
    adj_mat = np.zeros((np.prod(im.shape),) * 2)
    W = lat2W(*im.shape)
    adj_mat = W.full()[0].astype(bool)
    metric = im.flatten()
    return adj_mat, metric


def test_morans_i_image_rand():
    kernel = generate_binary_structure(2, 1)
    kernel[1, 1] = False
    assert np.isclose(
        morans_i_image(im_rand, kernel=kernel), -0.007927948045819038
    )


def test_morans_i_image_check():
    kernel = generate_binary_structure(2, 1)
    kernel[1, 1] = False
    assert np.isclose(
        morans_i_image(im_check, kernel=kernel), -0.9999999999999994
    )


def test_morans_i_image_check_inverted():
    kernel = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    assert np.isclose(morans_i_image(im_check, kernel=kernel), 1)


def test_morans_i_image_half():
    kernel = generate_binary_structure(2, 1)
    kernel[1, 1] = False
    assert np.isclose(
        morans_i_image(im_half, kernel=kernel), 0.9897289391169648
    )


def test_morans_i_graph_rand():
    adj_mat, metric = get_adj_metric(im_rand)
    assert np.isclose(
        morans_i_adjacency_matrix(adj_mat, metric), -0.007927948045819042
    )


def test_morans_i_graph_check():
    adj_mat, metric = get_adj_metric(im_check)
    assert np.isclose(
        morans_i_adjacency_matrix(adj_mat, metric), -0.9999999999999994
    )


def test_morans_i_graph_half():
    adj_mat, metric = get_adj_metric(im_half)
    assert np.isclose(
        morans_i_adjacency_matrix(adj_mat, metric), 0.9897289391169648
    )
