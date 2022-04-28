import matplotlib.pyplot as plt
from lagrange_polynomial_3d import LagrangePolynomial3D
from newton_polynomial_3d import NewtonPolynomial3D
from cubic_spline_3d import CubicSpline3D


if __name__ == '__main__':
    print('1. Lagrange')
    print('2. Newton')
    print('3. Newton + Lagrange')
    print('4. Cubic Spline')
    print('5. Cubic Spline + Lagrange')
    print('6. Cubic Spline + Newton')
    print('7. Cubic Spline + Newton + Lagrange')
    f = int(input())
    flags = [False, False, False]
    if f > 7 or f <= 0:
        exit(-1)
    if f >= 4:
        flags[2] = True
        f -= 4
    if f >= 2:
        flags[1] = True
        f -= 2
    if f >= 1:
        flags[0] = True
        f -= 1

    x_points = [-2, 1, 0, -1, 5, -4]
    y_points = [0, -2, 3, -4, 0, 5]
    z_points = [0, 1, 2, 3, 4, 5]
    fig = plt.figure(num="Interpolation")
    ax = fig.add_subplot(111, projection='3d')
    points, = ax.plot(x_points, y_points, z_points, "x", color="black")

    if flags[0]:
        curve_lagrange, = ax.plot(x_points, y_points, z_points, "-r", label='parametric curve')
        x_curve_points, y_curve_points, z_curve_points = LagrangePolynomial3D(x_points, y_points, z_points) \
            .calculate_points()
        curve_lagrange.set_data_3d(x_curve_points, y_curve_points, z_curve_points)
    if flags[1]:
        curve_newton, = ax.plot(x_points, y_points, z_points, "-g", label='parametric curve')
        x_curve_points, y_curve_points, z_curve_points = NewtonPolynomial3D(x_points, y_points, z_points) \
            .calculate_points()
        curve_newton.set_data_3d(x_curve_points, y_curve_points, z_curve_points)

    if flags[2]:
        curve_cubic, = ax.plot(x_points, y_points, z_points, "-b", label='parametric curve')
        x_curve_points, y_curve_points, z_curve_points = CubicSpline3D(x_points, y_points, z_points) \
            .calculate_points()
        curve_cubic.set_data_3d(x_curve_points, y_curve_points, z_curve_points)

    plt.show()
