from cubic_spline import *
from polynomial_2d import Polynomial2D


class CubicSpline2D(Polynomial2D):
    def __init__(self, x, y, num=500):
        super().__init__(x, y, num)
        self.sx = CubicSpline(self.params, x)
        self.sy = CubicSpline(self.params, y)
