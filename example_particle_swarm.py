import numpy as np
from pyswarm import pso

# max x + xy
# -x + 2yx <= 8
# 2x + y <= 14
# 2x - y <= 10
# 0 <= x <= 10
# 0 <= y <= 10
# x integer


def model_obj(x):
    # Negative sign to maximize
    # pen is a penalization if constraints are not met

    pen = 0

    x[0] = np.round(x[0], 0)  # To define an integer variable

    if not -x[0] + 2 * x[0] * x[1] <= 8:
        pen = np.inf
    if not 2 * x[0] + x[1] <= 14:
        pen = np.inf
    if not 2 * x[0] - x[1] <= 10:
        pen = np.inf

    return -(x[0] + x[0] * x[1]) + pen


def cons(x):
    # Constraints are defined in model_obj(x)
    return []


lb = [0, 0]
ub = [10, 10]
x0 = [0, 0]  # Initial point

xopt, fopt = pso(model_obj, lb, ub, x0, cons)

print("x = ", xopt[0])
print("y = ", xopt[1])
