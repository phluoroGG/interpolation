import matplotlib.pyplot as plt
from lagrange_polynomial_2d import LagrangePolynomial2D
from newton_polynomial_2d import NewtonPolynomial2D
from cubic_spline_2d import CubicSpline2D

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

    x_points = []
    y_points = []
    fig, ax = plt.subplots(figsize=(9, 9), num="Interpolation")

    if flags[0]:
        curve_lagrange, = ax.plot(x_points, y_points, "-r", label="spline")
    if flags[1]:
        curve_newton, = ax.plot(x_points, y_points, "-g", label="spline")
    if flags[2]:
        curve_cubic, = ax.plot(x_points, y_points, "-b", label="spline")
    points, = ax.plot(x_points, y_points, "x", color="black")

    def on_click(event):
        x_new_point, y_new_point = ax.transData.inverted().transform([event.x, event.y])
        if len(x_points) != 0 \
                and x_new_point == x_points[-1] and y_new_point == y_points[-1]:
            return
        x_points.append(x_new_point)
        y_points.append(y_new_point)

        if len(x_points) > 1 and len(x_points) == len(y_points):
            if flags[0]:
                x_curve_points, y_curve_points = LagrangePolynomial2D(x_points, y_points).calculate_points()
                curve_lagrange.set_xdata(x_curve_points)
                curve_lagrange.set_ydata(y_curve_points)
            if flags[1]:
                x_curve_points, y_curve_points = NewtonPolynomial2D(x_points, y_points).calculate_points()
                curve_newton.set_xdata(x_curve_points)
                curve_newton.set_ydata(y_curve_points)
            if flags[2]:
                x_curve_points, y_curve_points = CubicSpline2D(x_points, y_points).calculate_points()
                curve_cubic.set_xdata(x_curve_points)
                curve_cubic.set_ydata(y_curve_points)

        points.set_xdata(x_points)
        points.set_ydata(y_points)

        fig.canvas.draw()

    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
