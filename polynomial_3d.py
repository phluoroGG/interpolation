import numpy as np
from abc import ABC


class Polynomial3D(ABC):
    def __init__(self, x, y, z, num=500):
        self.params = self.__calculate_params(x, y, z)
        self.num = num
        self.sx = None
        self.sy = None
        self.sz = None

    def point(self, param):
        x = self.sx.point(param)
        y = self.sy.point(param)
        z = self.sz.point(param)
        return x, y, z

    def calculate_points(self):
        params = np.linspace(self.params[0], self.params[-1], self.num)

        result_x, result_y, result_z = [], [], []
        for param in params:
            point_x, point_y, point_z = self.point(param)
            result_x.append(point_x)
            result_y.append(point_y)
            result_z.append(point_z)

        return result_x, result_y, result_z

    def __calculate_params(self, x, y, z):
        dx = np.diff(x)
        dy = np.diff(y)
        dz = np.diff(z)
        self.ds = [np.sqrt(idx ** 2 + idy ** 2 + idz ** 2) for (idx, idy, idz) in zip(dx, dy, dz)]
        s = [0.0]
        s.extend(np.cumsum(self.ds))
        return s
