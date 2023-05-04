import turtle

import numpy as np

from .transformations import AffineTransformation

MAX_ITERATIONS = 11000


def run():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("green")
    pen.penup()

    affine = AffineTransformation()

    coordinates = np.array([0, 0, 1])
    for n in range(MAX_ITERATIONS):
        # Calculate new coordinates
        coordinates = np.matmul(coordinates, affine.transformation)
        print(coordinates)

        # Set last element as 1
        coordinates[-1] = 1

        # Increment x and y coordinates
        coordinates[:-1] += 1

        # Get x and y
        x, y, _ = coordinates

        # Draw the point
        pen.goto(4 * 65 * x, 4 * 37 * y - 252)  # scale the fern to fit inside the window
        pen.pendown()
        pen.dot(3)
        pen.penup()
