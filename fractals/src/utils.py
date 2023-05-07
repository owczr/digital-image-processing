import os
from PIL import Image

import numpy as np
from matplotlib.image import imsave

MAX_ITERATIONS = 1100000


def load_image(path):
    """Load image to numpy array"""
    image = Image.open(path)

    image_array = np.asarray(image)

    return image_array


def save_image(image_array, path, name):
    """Save numpy array as image"""
    filename = f"{name}.jpg"

    filepath = os.path.join(path, filename)

    imsave(filepath, image_array, cmap="gray")
