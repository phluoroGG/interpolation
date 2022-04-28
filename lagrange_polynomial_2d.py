from lagrange_polynomial import *
from polynomial_2d import Polynomial2D


class LagrangePolynomial2D(Polynomial2D):
    def __init__(self, x, y, num=500):
        super().__init__(x, y, num)
        self.sx = LagrangePolynomial(self.params, x)
        self.sy = LagrangePolynomial(self.params, y)
