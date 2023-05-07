import numpy as np

from .transformations import AffineTransformation
from .utils import load_image, MAX_ITERATIONS


def generate(path):
    # Load image and shape
    image = load_image(path)
    height, width = image.shape[:2]

    # Generate fractal points
    fractal_points = generate_points(height, width)

    # Center fractal points
    # fractal_points = center(fractal_points, height, width)

    # Scale fractal points to fill all image space
    fractal_points = scale(fractal_points, height, width)

    # Create fractal matrix
    fractal = generate_fractal(fractal_points, height, width)

    return fractal


def generate_fractal(points, height, width):
    # Define matrix to store calculated points
    fractal = np.zeros((height, width))

    for x, y in points:
        # Cast to integers
        x, y = int(x), int(y)

        # Draw the point
        fractal[y, x] = 1

    # Standardize values between 0 and 255
    fractal = standardize(fractal)

    return fractal


def generate_points(height, width):
    # Create object with affine transformations
    affine = AffineTransformation()

    # Set starting coordinates
    x = 100  # width // 2
    y = 200  # height // 2
    coordinates = np.array([x, y, 1])

    fractal_points = []

    for n in range(MAX_ITERATIONS):
        # Calculate new coordinates
        coordinates = np.matmul(affine.transformation, coordinates)

        # Set last element as 1
        coordinates[-1] = 1

        # Increment x and y coordinates
        coordinates[:-1] += 1

        # Get x and y
        x, y, _ = coordinates
        fractal_points.append((x, y))

    return fractal_points


def center(points, height, width):
    # Calculate midpoint
    x_sum = sum([point[0] for point in points])
    y_sum = sum([point[1] for point in points])
    midpoint = (x_sum / len(points), y_sum / len(points))

    # Calculate displacement
    dx = (width / 2) - midpoint[0]
    dy = (height / 2) - midpoint[1]

    # Move points to center
    centered_points = []
    for point in points:
        x = point[0] + dx
        y = point[1] + dy
        centered_points.append((x, y))

    return centered_points


def scale(points, width, height):
    x_coords, y_coords = zip(*points)
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)

    # Calculate scaling factors to fit the points within the given dimensions
    x_scale = width / (x_max - x_min)
    y_scale = height / (y_max - y_min)
    scale_factor = min(x_scale, y_scale)

    # Scale and re-center the points
    scaled_points = []
    for x, y in points:
        x_centered = x - (x_max + x_min) / 2
        y_centered = y - (y_max + y_min) / 2
        scaled_x = scale_factor * x_centered
        scaled_y = scale_factor * y_centered
        scaled_points.append((scaled_x, scaled_y))

    return scaled_points


def standardize(fractal):
    return (fractal - np.min(fractal)) * 255 / np.max(fractal)
