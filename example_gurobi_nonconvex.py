# To use Gurobi solver, it is necessary to download the license
# Gurobi works with LP
# It is able to solve some special cases, such as cone programming

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np

# min C1 + C2 + C3
# n1 + n2 + n3 = 2100
# C1 = 0.01n1**2 + 2n1
# C2 = 6n2n1 # Non convex constraint
# C3 = 7n3
# 0 <= n1,n2,n3 <= 1000
# n1,n2,n3 integers

model = pyo.ConcreteModel()

model.C = pyo.Var(range(1, 4))
model.n = pyo.Var(range(1, 4), within=Integers, bounds=(0, 1000))

C = model.c
n = model.n

# pyo.summation(C) is equivalent to C[1]+C[2]+C[3]
model.obj = pyo.Objective(expr=pyo.summation(C), sense=maximize)

model.total = pyo.Constraint(expr=pyo.summation(C) == 2100)
model.C1 = pyo.Constraint(expr=C[1] == 0.01 * n[1] * n[1] + 2 * n[1])
model.C2 = pyo.Constraint(expr=C[2] == 6 * n[2] * n[1])
model.C3 = pyo.Constraint(expr=C[3] == 7 * n[3])


opt = SolverFactory("gurobi")
opt.options["NonConvex"] = 2  # This is a parameter for the solver
opt.solve(model)

# Print results

print("n1=", pyo.value(n[1]))
print("n2=", pyo.value(n[2]))
print("n3=", pyo.value(n[3]))
print("nTotal=", pyo.summation(n))

print("C1=", pyo.value(C[1]))
print("C2=", pyo.value(C[2]))
print("C3=", pyo.value(C[3]))
print("CTotal=", pyo.summation(C))
