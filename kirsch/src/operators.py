import numpy as np


class Kirsch:
    def __int__(self):
        self.__operators = None

    @property
    def operators(self):
        return self.__operators

    @operators.getter
    def operators(self):
        operator = np.array([[-3, -3, 5],
                             [-3, 0, 5],
                             [-3, -3, 5]])
        return [
            operator,
            np.rot90(operator, 1),
            np.rot90(operator, 2),
            np.rot90(operator, 3),
            np.fliplr(operator),
            np.flipud(operator),
            np.fliplr(np.rot90(operator, 1)),
            np.flipud(np.rot90(operator, 1)),
        ]
