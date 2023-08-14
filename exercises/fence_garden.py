# Fence in the garden
# Mazimize area
# max xy
# 2x + y <= 100
# x,y >= 0

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0, None))
model.y = pyo.Var(bounds=(0, None))

x = model.x
y = model.y

model.C1 = pyo.Constraint(expr=2 * x + y <= 100)

model.obj = pyo.Objective(expr=x * y, sense=maximize)

opt = SolverFactory("ipopt", executable="/workspaces/optimization/ipopt_solver/ipopt")

opt.solve(model)

model.pprint()

print("x =", pyo.value(x))
print("y =", pyo.value(y))

print("Area = ", str(pyo.value(model.obj)))
