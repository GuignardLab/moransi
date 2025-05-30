import numpy as np
from scipy.ndimage import convolve
from scipy.sparse import sparray


def morans_i_image(
    image: np.ndarray, kernel: np.ndarray, hasnan: bool = False
) -> float:
    """Compute and return the Moran Index of `image` using `kernel` for the weights

    Parameters
    ----------
    image : np.ndarray
        The image to compute the moran index on
    kernel : np.ndarray
        The kernel from which the weights are computed from
    hasnan : bool
        whether or not `image` has nan values

    Returns
    -------
    float
        The moran index of the image `image` given the weights `kernel`
    """
    if hasnan:
        mask = np.isnan(image)
        image_ = image - np.nanmean(image)
        image = np.nan_to_num(image)
    else:
        image_ = image - np.mean(image)
    nb_neighb = 1 / convolve(mask.astype(float), kernel, mode="constant")
    nb_neighb[mask] = 0
    C = (nb_neighb) * convolve(image_, kernel, mode="constant")
    M = np.sum(image_ * C) / np.sum(image_**2)
    return M


def morans_i_adjacency_matrix(
    adj_mat: np.ndarray | sparray, metric: np.ndarray
) -> float:
    """Compute and returns the Moran Index of a given graph and a given metric on the nodes

    The graph is expected as an adjacency matrix `adj` where `adj[i, j]`
    is the weight of the link between the nodes `i` and `j`.

    The metric is expected to be an array `m` where `m[i]` is the value
    of the metric for the node `i`.

    Parameters
    ----------
    adj_mat : np.ndarray or sparray of size N x N
        The adjacency matrix of the graph that has `N` nodes
    metric : np.ndarray of size N
        The array where are stored the metrics

    Returns
    -------
    float
        The moran index of the image `image` given the weights `kernel`
    """
    avg = np.mean(metric)
    metric_ = metric - avg

    return (
        np.sum((adj_mat @ metric_) * metric_ / adj_mat.sum(axis=0))
    ) / np.sum(metric_**2)
