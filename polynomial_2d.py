import numpy as np
from abc import ABC


class Polynomial2D(ABC):
    def __init__(self, x, y, num=500):
        self.params = self.__calculate_params(x, y)
        self.num = num
        self.sx = None
        self.sy = None

    def point(self, param):
        x = self.sx.point(param)
        y = self.sy.point(param)
        return x, y

    def calculate_points(self):
        params = np.linspace(self.params[0], self.params[-1], self.num)

        result_x, result_y = [], []
        for param in params:
            point_x, point_y = self.point(param)
            result_x.append(point_x)
            result_y.append(point_y)

        return result_x, result_y

    def __calculate_params(self, x, y):
        dx = np.diff(x)
        dy = np.diff(y)
        self.ds = [np.sqrt(idx ** 2 + idy ** 2) for (idx, idy) in zip(dx, dy)]
        s = [0.0]
        s.extend(np.cumsum(self.ds))
        return s
