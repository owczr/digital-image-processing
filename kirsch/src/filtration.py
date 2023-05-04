import numpy as np
from scipy.signal import convolve2d

from .operators import Kirsch
from .utils import is_rgb, is_near_boundary


# FIXME: Filtrated images seem distorted

def filtrate_image(image_array):
    kirsch = Kirsch()

    filtration = np.zeros_like(image_array)

    if is_rgb(image_array):
        return filtrate_rgb(image_array, kirsch, filtration)
    return filtrate_greyscale(image_array, kirsch, filtration)


def filtrate_greyscale(image_array, kirsch, filtration):
    image_array = add_symmetric_boundary(image_array)

    pixels = np.ndindex(image_array.shape[0], image_array.shape[1])

    for y, x in pixels:
        if is_near_boundary(x, y, image_array):
            continue

        kirsch_response = calculate_kirsch_responses(x, y, image_array, kirsch)

        filtration[y][x] = kirsch_response

    return filtration


def filtrate_rgb(image_rgb, kirsch, filtration):
    channels = image_rgb.shape[2]

    for channel in range(channels):
        image_array = image_rgb[:, :, channel]
        image_array = add_symmetric_boundary(image_array)

        pixels = np.ndindex(image_array.shape[0], image_array.shape[1])

        for y, x in pixels:
            if is_near_boundary(x, y, image_array):
                continue

            kirsch_response = calculate_kirsch_responses(x, y, image_array, kirsch)

            filtration[y][x][channel] = kirsch_response

    return filtration


def calculate_kirsch_responses(x, y, image_array, kirsch):
    kirsch_responses = []

    for operator in kirsch.operators:
        patch = image_array[y - 1: y + 2, x - 1: x + 2]
        kirsch_response = np.max(convolve2d(patch, operator, mode='same'))
        kirsch_responses.append(kirsch_response)

    return sum(kirsch_responses)


def add_symmetric_boundary(image_array):
    image_array = np.pad(image_array, pad_width=1, mode='symmetric')
    return image_array
