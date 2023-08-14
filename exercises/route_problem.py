# Problem from examples/example_genetic_shortest_path.ipynb

import pandas as pd

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory


# Inputs
nodes = pd.read_excel("../data/route_inputs.xlsx", sheet_name="nodes")
paths = pd.read_excel("../data/route_inputs.xlsx", sheet_name="paths")
n_paths = len(paths)

# Model
model = pyo.ConcreteModel()

# Variables
model.x = pyo.Var(range(n_paths), within=Binary)
x = model.x

# Constraints

# Origin
node_origin = int(nodes.node[nodes.description == "origin"])
model.C1 = pyo.Constraint(
    expr=sum([x[p] for p in paths.index[paths.node_from == node_origin]]) == 1
)

# Destination
node_destination = int(nodes.node[nodes.description == "destination"])
model.C2 = pyo.Constraint(
    expr=sum([x[p] for p in paths.index[paths.node_to == node_destination]]) == 1
)

# Intermidiate

model.C3 = pyo.ConstraintList()
for node in nodes.node[nodes.description == "middle point"]:
    sum_in = sum([x[p] for p in paths.index[paths.node_to == node]])
    sum_out = sum([x[p] for p in paths.index[paths.node_from == node]])

    model.C3.add(expr=sum_in == sum_out)


# Objective function

distance = sum([x[p] * paths.distance[p] for p in paths.index])
model.obj = pyo.Objective(expr=distance, sense=minimize)

# Solver

opt = SolverFactory("glpk")
results = opt.solve(model)


# model.pprint()

# Print results

paths["activated"] = 0
for p in paths.index:
    paths.activated[p] = pyo.value(x[p])

print("\n\nAll Paths:")
print(paths)

print("\nSelected Paths:")
print(paths[paths.activated == 1])

print("\nTotal path:", pyo.value(model.obj))
