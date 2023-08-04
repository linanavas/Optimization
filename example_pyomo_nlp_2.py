# IPOPT finds local solution, not the global
# Different variable initializations return different solutions

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(-5, 5), initialize=0)
model.y = pyo.Var(bounds=(-5, 5), initialize=0)

x = model.x
y = model.y


model.obj = pyo.Objective(expr=cos(x + 1) + cos(x) * cos(y), sense=maximize)

opt = SolverFactory("ipopt", executable="/workspaces/optimization/ipopt_solver/ipopt")
opt.options["tol"] = 1e-6
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print("x=", x_value)
print("y=", y_value)
