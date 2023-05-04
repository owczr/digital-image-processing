from PIL import Image

import numpy as np


def load_image(path):
    image = Image.open(path)

    image_array = np.asarray(image)

    return image_array


def is_rgb(image):
    return len(image.shape) == 3


def is_near_boundary(x, y, image_array):
    return y < 1 or y >= image_array.shape[0] - 2 or x < 1 or x >= image_array.shape[1] - 2
