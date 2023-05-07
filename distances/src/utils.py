from PIL import Image

import numpy as np


def load_binary_image(path):
    """Load image to binary numpy array"""
    image = Image.open(path)

    image_array = np.asarray(image)

    return image_array > 0