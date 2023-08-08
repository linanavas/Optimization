import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np

# min C1 + C2 + C3
# n1 + n2 + n3 = 2100
# C1 = 2n1
# C2 = 6n2 + 1000b
# C3 = 7n3
# n2 <= 1000b
# 0 <= n1,n2,n3 <= 1000
# n1,n2,n3 integers
# b is binary

model = pyo.ConcreteModel()

model.C = pyo.Var(range(1, 4))
model.n = pyo.Var(range(1, 4), within=Integers, bounds=(0, 1000))
model.b = pyo.Var(within=Binary)

C = model.C
n = model.n
b = model.b

# pyo.summation(C) is equivalent to C[1]+C[2]+C[3]
model.obj = pyo.Objective(expr=pyo.summation(C), sense=minimize)

model.total = pyo.Constraint(expr=pyo.summation(n) == 2100)
model.C1 = pyo.Constraint(expr=C[1] == 2 * n[1])
model.C2 = pyo.Constraint(expr=C[2] == 6 * n[2] + 1000 * b)
model.C3 = pyo.Constraint(expr=C[3] == 7 * n[3])
model.C4 = pyo.Constraint(expr=n[2] <= 1000 * b)

opt = SolverFactory("glpk")
opt.solve(model)

# Print results

print("n1=", pyo.value(n[1]))
print("n2=", pyo.value(n[2]))
print("n3=", pyo.value(n[3]))
print("nTotal=", pyo.value(pyo.summation(n)))
print("b=", pyo.value(b))

print("C1=", pyo.value(C[1]))
print("C2=", pyo.value(C[2]))
print("C3=", pyo.value(C[3]))
print("CTotal=", pyo.value(pyo.summation(C)))
