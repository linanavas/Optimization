import pandas as pd

import pyomo.environ as pyo

# from pyomo.environ import *
from pyomo.opt import SolverFactory


# Sets
machines = range(1, 4 + 1)
hours = range(1, 10 + 1)

# Model
model = pyo.ConcreteModel()

# Variables
model.x = pyo.Var(machines, hours, within=pyo.Integers, bounds=(0, 10))
x = model.x

# Objective function
total_producton = sum([x[m, t] for m in machines for t in hours])
model.obj = pyo.Objective(expr=total_producton, sense=pyo.maximize)

# Constraint 1
model.C1 = pyo.ConstraintList()
for t in hours:
    model.C1.add(expr=2 * x[2, t] - 8 * x[3, t] <= 0)

# Constraint 2
model.C2 = pyo.ConstraintList()
for t in hours:
    if t > 2:
        model.C2.add(expr=x[2, t] - 2 * x[3, t - 2] + x[4, t] >= 1)

# Constraint 3
model.C3 = pyo.ConstraintList()
for t in hours:
    model.C3.add(expr=sum([x[m, t] for m in machines]) <= 50)

# Constraint 4
model.C4 = pyo.ConstraintList()
for t in hours:
    if t > 1:
        model.C4.add(expr=x[1, t] + x[2, t - 1] + x[3, t] + x[4, t] <= 10)

# Bounds could be replaced by an inequality constraint
# model.C5 = pyo.ConstraintList()
# for t in hours:
#    for m in machines:
#        model.C5.add(pyo.inequality(0,x[m,t],10))

# Solver

opt = SolverFactory("glpk")
# opt.options['MIPgap'] = 0.0001 # Gurobi parameter for gap tolerance
# opt.options['Time Limit'] = 60 # Gurobi parameter for limit time in seconds

results = opt.solve(model, tee=True)
# tee = True Information about the solver

# model.pprint()

# Print results

# for m in machines:
#    for t in hours:
#        print("x" + str(m) + "," + str(t) + " = " + str(pyo.value(x[m, t])))

print()
print("Production = ", str(pyo.value(model.obj)))
