import matplotlib.pyplot as plt
from cubic_spline_3d import *


def calculate_3d_spline_interpolation(x, y, z, num=500):
    cubic_spline_3d = CubicSpline3D(x, y, z)
    params = np.linspace(cubic_spline_3d.params[0], cubic_spline_3d.params[-1], num)

    result_x, result_y, result_z = [], [], []
    for param in params:
        point_x, point_y, point_z = cubic_spline_3d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)
        result_z.append(point_z)

    return result_x, result_y, result_z


if __name__ == '__main__':
    x_points = [0, 1, 2, 3]
    y_points = [-1, -3, 2, 0]
    z_points = [5, 3, -2, 1]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    curve, = ax.plot(x_points, y_points, z_points, "-g", label='parametric curve')
    points, = ax.plot(x_points, y_points, z_points, "x")

    x_curve_points, y_curve_points, z_curve_points = calculate_3d_spline_interpolation(x_points, y_points, z_points)
    curve.set_data_3d(x_curve_points, y_curve_points, z_curve_points)

    plt.show()
