from cubic_spline import *
from polynomial_3d import Polynomial3D


class CubicSpline3D(Polynomial3D):
    def __init__(self, x, y, z, num=500):
        super().__init__(x, y, z, num)
        self.sx = CubicSpline(self.params, x)
        self.sy = CubicSpline(self.params, y)
        self.sz = CubicSpline(self.params, z)

