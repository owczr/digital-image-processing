from PIL import Image

import numpy as np


def load_image(path):
    """Load image to numpy array"""
    image = Image.open(path)

    image_array = np.asarray(image)

    return image_array


def is_binary(image):
    unique_values = np.unique(image)
    return np.array_equal(unique_values, np.array([0, 1]))
