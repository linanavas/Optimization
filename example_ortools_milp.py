from ortools.linear_solver import pywraplp

# GLOP solver does not support MILP problems, use CBC, Gurobi or CPLEX
solver = pywraplp.Solver.CreateSolver("CBC")

# Variables

x = solver.IntVar(0, 10, "x")
y = solver.NumVar(0, 10, "y")


# Constraints

solver.Add(-x + 2 * y <= 7)
solver.Add(2 * x + y <= 14)
solver.Add(2 * x - y <= 10)

# Objective function

solver.Maximize(x + y)

# Solve

results = solver.Solve()

if results == pywraplp.Solver.OPTIMAL:
    print("Optimal Found")

print("x", x.solution_value())
print("y", y.solution_value())
