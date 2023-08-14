# Same problem as example_pyomo_advanced.py
# Organized using rules

import pandas as pd

import pyomo.environ as pyo

# from pyomo.environ import *
from pyomo.opt import SolverFactory

# =====================================================================================
# Rules functions
# =====================================================================================


def myrule1(model, t):
    return 2 * model.x[2, t] - 8 * model.x[3, t] <= 0


def myrule2(model, t):
    return model.x[2, t] - 2 * model.x[3, t - 2] + model.x[4, t] >= 1


def myrule3(model, t):
    return sum([model.x[m, t] for m in model.setM]) <= 50


def myrule4(model, t):
    return model.x[1, t] + model.x[2, t - 1] + model.x[3, t] + model.x[4, t] <= 10


def myrule5(model, m, t):
    return pyo.inequality(0, model.x[m, t], 10)


# =====================================================================================
# Model
# =====================================================================================

model = pyo.ConcreteModel()

# Pyomo parameters
model.T = pyo.Param(initialize=10)
model.M = pyo.Param(initialize=4)

# Pyomo sets
model.setT = pyo.Set(initialize=range(1, model.T + 1))
model.setM = pyo.Set(initialize=range(1, model.M + 1))

# Variables
model.x = pyo.Var(
    model.setM, model.setT, within=pyo.Integers
)  # Bounds will be managed as constraints

# Objective function
model.obj = pyo.Objective(expr=pyo.summation(model.x), sense=pyo.maximize)

# Constraints
model.C1 = pyo.Constraint(model.setT, rule=myrule1)
model.C2 = pyo.Constraint(range(3, model.T + 1), rule=myrule2)
model.C3 = pyo.Constraint(model.setT, rule=myrule3)
model.C4 = pyo.Constraint(range(2, model.T + 1), rule=myrule4)
model.C5 = pyo.Constraint(model.setM, model.setT, rule=myrule5)

# Solver

opt = SolverFactory("glpk")
results = opt.solve(model, tee=True)

# model.pprint()

# Print results

print()
print("Production = ", str(pyo.value(model.obj)))
