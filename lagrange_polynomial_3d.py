from lagrange_polynomial import *
from polynomial_3d import Polynomial3D


class LagrangePolynomial3D(Polynomial3D):
    def __init__(self, x, y, z, num=500):
        super().__init__(x, y, z, num)
        self.sx = LagrangePolynomial(self.params, x)
        self.sy = LagrangePolynomial(self.params, y)
        self.sz = LagrangePolynomial(self.params, z)
