from PIL import Image

import numpy as np

MAX_ITERATIONS = 1100000


def load_image(path):
    """Load image to numpy array"""
    image = Image.open(path)

    image_array = np.asarray(image)

    return image_array

