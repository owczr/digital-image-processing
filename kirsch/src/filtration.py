import numpy as np

from .operators import Kirsch
from .utils import is_rgb, is_greyscale, is_near_boundary


def filtrate_image(image_array):
    # Create object with kirsch operators
    kirsch = Kirsch()

    # Define array to store kirsch responses
    filtration = np.zeros_like(image_array)

    if is_rgb(image_array):
        return filtrate_rgb(image_array, kirsch, filtration)
    elif is_greyscale(image_array):
        return filtrate_greyscale(image_array, kirsch, filtration)
    else:
        raise ValueError("Unsupported number of channels")


def filtrate_greyscale(image_array, kirsch, filtration):
    # Pad image with symmetric boundary
    image_array = add_symmetric_boundary(image_array)

    # Get all indexes
    pixels = np.ndindex(image_array.shape[0], image_array.shape[1])

    # Loop over all pixels and calculate convolution with kirsch operators
    for y, x in pixels:
        if is_near_boundary(x, y, image_array):
            continue

        kirsch_response = calculate_kirsch_responses(x, y, image_array, kirsch)

        filtration[y][x] = kirsch_response

    return filtration


def filtrate_rgb(image_rgb, kirsch, filtration):
    # Get number of channels
    channels = image_rgb.shape[2]

    # Loop over all channels and apply greyscale filtration
    for channel in range(channels):
        image_array = image_rgb[:, :, channel]
        filtration_grey = np.zeros_like(image_array)
        filtration[:, :, channel] = filtrate_greyscale(image_array, kirsch, filtration_grey)

    return filtration


def calculate_kirsch_responses(x, y, image_array, kirsch):
    """Loops over all kirsch operators, calculates convolution and returns maximum"""
    kirsch_responses = []

    for operator in kirsch.operators:
        patch = image_array[y - 1: y + 2, x - 1: x + 2]
        kirsch_response = convolve(operator, patch)
        kirsch_responses.append(kirsch_response)

    return np.max(kirsch_responses)


def convolve(operator, image_array):
    response = 0
    for i in range(3):
        for j in range(3):
            response += operator[j][i] * image_array[j][i]

    return response


def add_symmetric_boundary(image_array):
    image_array = np.pad(image_array, pad_width=1, mode='symmetric')
    return image_array
