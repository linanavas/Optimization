import numpy as np
from geneticalgorithm import geneticalgorithm as ga

# max x + xy
# -x + 2yx <= 8
# 2x + y <= 14
# 2x - y <= 10
# 0 <= x <= 10
# 0 <= y <= 10
# x integer


def f(x):
    # Negative sign to maximize
    # pen is a penalization if constraints are not met

    pen = 0

    if not -x[0] + 2 * x[0] * x[1] <= 8:
        pen = np.inf
    if not 2 * x[0] + x[1] <= 14:
        pen = np.inf
    if not 2 * x[0] - x[1] <= 10:
        pen = np.inf

    return -(x[0] + x[0] * x[1]) + pen


varbounds = np.array([[0, 10], [0, 10]])
vartype = np.array([["int"], ["real"]])

model = ga(
    function=f, dimension=2, variable_type_mixed=vartype, variable_boundaries=varbounds
)

model.run()
