import pandas as pd

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory


# Inputs
dataGen = pd.read_csv("data/generators.csv")
dataLoad = pd.read_csv("data/load.csv")

Ng = len(dataGen)

# Model
model = pyo.ConcreteModel()

# Variables
model.Pg = pyo.Var(range(Ng), bounds=(0, None))
Pg = model.Pg

# Constraints
pg_sum = sum([Pg[g] for g in dataGen["id"]])
print(pg_sum)

model.balance = pyo.Constraint(expr=pg_sum == sum(dataLoad["value"]))

model.cond = pyo.Constraint(expr=Pg[0] + Pg[3] >= dataLoad["value"][0])

model.limits = pyo.ConstraintList()

for g in dataGen["id"]:
    model.limits.add(expr=Pg[g] <= dataGen["limit"][g])

# Objective function
cost_sum = sum([Pg[g] * dataGen["cost"][g] for g in dataGen["id"]])
model.obj = pyo.Objective(expr=cost_sum)

# Solver

opt = SolverFactory("glpk")
results = opt.solve(model)


model.pprint()

# Print results

dataGen["Pg"] = [pyo.value(Pg[g]) for g in dataGen["id"]]
print(dataGen)

print(results)
print("Final objective value: ", value(model.obj))
