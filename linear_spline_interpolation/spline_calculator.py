import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """
    The actual function f(x) that we are approximating with the spline.
    You can define your actual function here.
    """
    return np.exp(x)  # Example function


def linear_spline(x_points, y_points):
    """
    Computes linear splines for given x and y points and prints each step.

    Args:
    x_points : list or array-like, contains the x-coordinates of the points
    y_points : list or array-like, contains the y-coordinates of the points

    Returns:
    splines : list of tuples (a, b, interval), where each tuple represents
              the linear spline in the form y = a*x + b for a particular interval
    """
    n = len(x_points) - 1
    k = 3
    splines = []

    for i in range(n):
        # Calculate the spline
        h = x_points[i+1]- x_points[i]
        s = (y_points[i+1]+(k-1)*y_points[i])/k
        func = f(x_points[i]+h/k)
        # Calculate the absolute error
        abs_error = abs(s-func)

        # Store the spline in the form y = a*x + b for the interval [x_i, x_(i+1)]
        spline = (s, (x_points[i], x_points[i + 1]))
        splines.append(spline)

        # Print the calculation details
        print(f"Spline number #{i}: {s}")
        print(f"Spline absolute error: {abs_error}")
        print(f"Interval: [{x_points[i]}, {x_points[i + 1]}]")
        print()

    return splines

# Example usage:
a = -1; b = 1; n = 5; step = (b-a)/n
x_points = [round(c,2) for c in np.arange(a,b + step,step)]
y_points = [f(x) for x in x_points]  # Using the actual function f(x) to generate y-points
print(x_points, '\n', y_points)
# Calculate the linear splines
splines = linear_spline(x_points, y_points)
