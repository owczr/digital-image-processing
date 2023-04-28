import numpy as np


class AffineTransformation:
    """Class that returns random affine transformation matrix"""
    def __init__(self):
        self.__transformation = None
        self.__matrices = [
            np.array([[-.67, -.82, 0],
                      [-.18, 0.81, 10],
                      [0, 0, 1]]),
            np.array([[.4, .4, 0],
                      [-.1, .4, 0],
                      [0, 0, 0]]),
            np.array([[-.4, -.4, 0],
                      [-.1, .4, 0],
                      [0, 0, 0]]),
            np.array([[-.1, 0, 0],
                      [.44, .44, -2],
                      [0, 0, 1]])
        ]

    @property
    def transformation(self):
        return self.__transformation

    @transformation.getter
    def transformation(self):
        matrix_index = np.random.randint(0, 4)
        return self.__matrices[matrix_index]
