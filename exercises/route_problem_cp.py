# Constraint programming
# Problem from examples/example_genetic_shortest_path.ipynb

import pandas as pd
import numpy as np
from ortools.sat.python import cp_model


# Inputs
nodes = pd.read_excel("../data/route_inputs.xlsx", sheet_name="nodes")
paths = pd.read_excel("../data/route_inputs.xlsx", sheet_name="paths")
n_nodes = len(nodes)
n_paths = len(paths)

# Model
model = cp_model.CpModel()

# It is necessary to define an upper bound
x = np.zeros(n_paths).tolist()

for p in paths.index:
    x[p] = model.NewIntVar(0, 1, "x[{}]".format([p]))

# Objective function
objFun = sum([x[p] * paths.distance[p] for p in paths.index])
model.Minimize(objFun)

# Constraints
node_origin = int(nodes.node[nodes.description == "origin"])
node_destination = int(nodes.node[nodes.description == "destination"])

model.Add(sum([x[p] for p in paths.index[paths.node_from == node_origin]]) == 1)
model.Add(sum([x[p] for p in paths.index[paths.node_to == node_destination]]) == 1)

for node in nodes.node[nodes.description == "middle point"]:
    sum_in = sum([x[p] for p in paths.index[paths.node_to == node]])
    sum_out = sum([x[p] for p in paths.index[paths.node_from == node]])
    model.Add(sum_in == sum_out)

# Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Print
print("Status = ", solver.StatusName(status))
print("OF = ", solver.ObjectiveValue())

paths["activated"] = 0
for p in paths.index:
    paths.activated[p] = solver.Value(x[p])

print("\n\nAll Paths:")
print(paths)

print("\nSelected Paths:")
print(paths[paths.activated == 1])
