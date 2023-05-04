import turtle

import numpy as np

from .transformations import AffineTransformation

MAX_ITERATIONS = 11000


def run():
    pen = create_pen()
    affine = AffineTransformation()
    coordinates = np.array([0, 0, 1])

    for n in range(MAX_ITERATIONS):
        # Calculate new coordinates
        coordinates = np.matmul(coordinates, affine.transformation)

        # Set last element as 1
        coordinates[-1] = 1

        # Increment x and y coordinates
        coordinates[:-1] += 1

        # Get x and y
        x, y, _ = coordinates

        # Draw the point
        draw_point(pen, x, y)


def create_pen():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("green")
    pen.penup()

    return pen


def draw_point(pen, x, y):
    pen.goto(4 * 65 * x, 4 * 37 * y - 252)  # scale the fern
    pen.pendown()
    pen.dot(3)
    pen.penup()
