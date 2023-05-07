import numpy as np

from .logical import dilation
from .element import StructuralElement


def create_geodetic_map(binary_image, point, radius):
    # Create structural element
    structure = StructuralElement(radius=radius).element

    # Get starting coordinates
    x, y = point

    # Create output array
    geodetic_map = np.zeros_like(binary_image)

    # Set point coordinates to 1
    geodetic_map[x, y] = 1

    # Perform and operation on dilated output array and input image
    first_dilation = dilation(geodetic_map, structure)

    # Fill output array with zeros
    geodetic_map = np.zeros_like(binary_image, dtype=np.uint8)

    distance = 0
    while True:
        # Perform and operation on previous dilation and input image
        second_dilation = dilation(first_dilation, structure) & binary_image

        # Subtract dilated images
        dilation_difference = np.abs(np.subtract(second_dilation, first_dilation))

        # Check for differences
        if dilation_difference.sum() == 0:
            break

        # Set second dilation to first dilation
        first_dilation = second_dilation

        # Set geodetic map points
        for x, y in np.argwhere(dilation_difference == 1):
            geodetic_map[x, y] = distance

        # Increment distance
        distance += 1

    # Set starting point as 0
    geodetic_map[x, y] = 0

    return geodetic_map
