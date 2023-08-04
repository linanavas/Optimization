from pyomo.environ import *

# Create a Pyomo model
model = ConcreteModel()

# Define decision variables
model.x = Var(within=NonNegativeReals)

# Define the objective function
model.objective = Objective(expr=model.x**2 - 4 * model.x, sense=minimize)

# Solve the optimization problem with Ipopt
solver = SolverFactory(
    "ipopt", executable="/workspaces/optimization/ipopt_solver/ipopt"
)
results = solver.solve(model)

# Print the results
print("Optimal value of x:", value(model.x))
print("Optimal objective value:", value(model.objective))
