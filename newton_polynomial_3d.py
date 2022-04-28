from newton_polynomial import *
from polynomial_3d import Polynomial3D


class NewtonPolynomial3D(Polynomial3D):
    def __init__(self, x, y, z, num=500):
        super().__init__(x, y, z, num)
        self.sx = NewtonPolynomial(self.params, x)
        self.sy = NewtonPolynomial(self.params, y)
        self.sz = NewtonPolynomial(self.params, z)
