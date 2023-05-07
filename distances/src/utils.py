import os
from PIL import Image

import numpy as np
from matplotlib.image import imsave


def load_binary_image(path):
    """Load image to binary numpy array"""
    image = Image.open(path)

    image_array = np.asarray(image)

    return image_array > 0


def save_image(image_array, path, name):
    """Save numpy array as image"""
    filename = f"{name}.jpg"

    filepath = os.path.join(path, filename)

    imsave(filepath, image_array, cmap="inferno")
