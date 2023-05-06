import numpy as np


class StructuralElement:
    def __init__(self, radius):
        self.radius = radius
        self.center = [radius, radius]
        self.__diameter = None
        self.__element = None

    @property
    def diameter(self):
        return self.__diameter

    @diameter.getter
    def diameter(self):
        return 2 * self.radius + 1

    @property
    def element(self):
        return self.__element

    @element.getter
    def element(self):
        if self.__element is not None:
            return self.__element

        # Generate a grid of coordinates
        grid = np.indices((self.diameter, self.diameter)) - np.array(self.center)[:, np.newaxis, np.newaxis]

        # Compute the distance from each point to the center
        distances = np.sqrt(np.sum(grid ** 2, axis=0))

        # Generate the binary structuring element
        struct = distances <= self.radius

        self.__element = struct.astype(int)

        return self.__element
