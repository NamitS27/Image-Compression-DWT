# pylint: disable=E0401
'Utility methods for the project'
from PIL import Image
import numpy as np

def load_img(path):
    """
    Returns an Image object if path is an existing image, otherwise None
    Parameters
    ----------
    path: string
        image path to open
    Returns
    -------
    Image:
        image object
    """
    try:
        return Image.open(path)
    except IOError:
        return None

def max_ndarray(mat):
    """
    Returns maximum value within a given 2D Matrix, otherwise 0
    Parameters
    ----------
    mat: numpy.ndarray
        matrix from which we want to compute the max value
    Returns
    -------
    int32:
        matrix maximum value
    """
    return np.amax(mat) if type(mat).__name__ == 'ndarray' else 0
