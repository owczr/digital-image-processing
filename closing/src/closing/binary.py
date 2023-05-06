import numpy as np

from ..element import StructuralElement


def closing(image, radius):
    structure = create_structural_element(radius)

    # Perform erosion
    eroded = erosion(image, structure)

    # Perform dilation
    closed = dilation(eroded, structure)

    return closed


def erosion(image, structure):
    return apply_structural_element(image, structure, np.all)


def dilation(image, structure):
    return apply_structural_element(image, structure, np.any)


def create_structural_element(radius):
    structural_element = StructuralElement(radius)
    return structural_element.element


def apply_structural_element(image, structure, func):
    # Cast input to boolean
    image = np.asarray(image, dtype=int)
    structure = np.asarray(structure, dtype=int)

    # Pad the image with zeros
    pad_width = ((structure.shape[0] // 2, structure.shape[0] // 2), (structure.shape[1] // 2, structure.shape[1] // 2))
    image_padded = np.pad(image, pad_width, mode='constant', constant_values=0)

    # Create output array
    output = np.zeros_like(image)

    # Iterate over the image
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            # Extract the patch from the image
            patch = image_padded[y:y + structure.shape[0], x:x + structure.shape[1]]

            # Apply the structural element
            output[y, x] = func(patch[structure])

    return output
