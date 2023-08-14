# Revenue
# N = Number of cars, p = Price
# max Np
# N = 1001-5p
# 50 <= p <=200
# N integer

# ipopt cannot deal with integers
# Cuoenne solves MINLP but there are issues with the installation

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.p = pyo.Var(bounds=(50, 200))
model.N = pyo.Var(within=Integers, bounds=(0, None))

p = model.p
N = model.N

model.C1 = pyo.Constraint(expr=1001 - 5 * p == N)

model.obj = pyo.Objective(expr=N * p, sense=maximize)

opt = SolverFactory("ipopt", executable="/workspaces/optimization/ipopt_solver/ipopt")

opt.solve(model)

model.pprint()

print("Price =", pyo.value(p))
print("Number of cars =", pyo.value(N))

print("Revenue = ", str(pyo.value(model.obj)))
