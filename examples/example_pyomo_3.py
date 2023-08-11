import numpy as np
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory


# Model
model = pyo.ConcreteModel()

# Variables
n = 5
model.x = pyo.Var(range(n), within=Integers, bounds=(0, None))
x = model.x

model.y = pyo.Var(bounds=(0, None))
y = model.y

# Constraints

sum_x = sum([x[i] for i in range(n)])
model.C1 = pyo.Constraint(expr=sum_x + y <= 20)

model.C2 = pyo.ConstraintList()

for i in range(5):
    model.C2.add(expr=x[i] + y >= 15)

sum_ix = sum([(i + 1) * x[i] for i in range(n)])

model.C3 = pyo.Constraint(expr=sum_ix >= 10)

model.C4 = pyo.Constraint(expr=x[4] + 2 * y >= 30)

# Objective function

model.obj = pyo.Objective(expr=sum_x + y, sense=minimize)

# Solver

opt = SolverFactory("glpk")
results = opt.solve(model)

model.pprint()

# Results

print("x: ", [pyo.value(x[i]) for i in range(n)])

print("y: ", pyo.value(y))
