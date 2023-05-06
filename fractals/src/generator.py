import numpy as np

from .transformations import AffineTransformation
from .utils import load_image, MAX_ITERATIONS


def generate(path):
    # Load image and shape
    image = load_image(path)
    height, width = image.shape[:2]

    # Define matrix to store calculated points
    fractal = np.zeros((height, width))

    # Create object with affine transformations
    affine = AffineTransformation()

    # Set starting coordinates
    x = np.random.randint(0, width)
    y = np.random.randint(0, height)
    coordinates = np.array([x, y, 1])

    for n in range(MAX_ITERATIONS):
        # Calculate new coordinates
        coordinates = np.matmul(affine.transformation, coordinates)

        # Set last element as 1
        coordinates[-1] = 1

        # Increment x and y coordinates
        coordinates[:-1] += 1

        # Get x and y
        x, y, _ = coordinates

        # Scale and center x and y
        x *= 20 * x + width / 2
        y *= 20 * y + height / 2

        # Cast to integers
        x, y = int(x), int(y)

        # Check bounding box
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        # Draw the point
        fractal[y, x] += 1

    fractal = scale_fractal(fractal)

    return fractal


def scale_fractal(fractal):
    return (fractal - np.min(fractal)) * 255 / np.max(fractal)
