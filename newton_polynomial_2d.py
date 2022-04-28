from newton_polynomial import *
from polynomial_2d import Polynomial2D


class NewtonPolynomial2D(Polynomial2D):
    def __init__(self, x, y, num=500):
        super().__init__(x, y, num)
        self.sx = NewtonPolynomial(self.params, x)
        self.sy = NewtonPolynomial(self.params, y)
