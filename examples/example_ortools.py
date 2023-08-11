from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")

# Variables

x = solver.NumVar(0, 10, "x")
y = solver.NumVar(0, 10, "y")


# Constraints

solver.Add(-x + 2 * y <= 8)
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
