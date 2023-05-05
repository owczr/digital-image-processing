import numpy as np


class Kirsch:
    """Calculates all kirsch operators by rotating two matrices"""
    def __int__(self):
        self.__operators = None

    @property
    def operators(self):
        return self.__operators

    @operators.getter
    def operators(self):
        operator = np.array([[5, 5, 5],
                             [-3, 0, -3],
                             [-3, -3, -3]])

        operator45 = np.array([[-3, 5, 5],
                               [-3, 0, 5],
                               [-3, -3, -3]])

        return [
            operator,
            operator45,
            np.rot90(operator),
            np.rot90(operator45),
            np.rot90(operator, 2),
            np.rot90(operator45, 2),
            np.rot90(operator, 3),
            np.rot90(operator45, 3)
        ]
