# Constraint programming
# CP solver only allows integer coefficientes

# max 2x + 2y + 3z
# x + (7/2)y + (3/2)z <= 25
# 3x - 5y + 7z <= 45
# 5x + 2y - 6z <= 37
# x,y,z >= 0
# x,y,z integers

from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions"""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print("%s=%i" % (v, self.Value(v)), end=" ")
        print()

    def solution_count(self):
        return self.__solution_count


model = cp_model.CpModel()

# It is necessary to define an upper bound
x = model.NewIntVar(0, 1000, "x")
y = model.NewIntVar(0, 1000, "y")
z = model.NewIntVar(0, 1000, "z")

model.Add(2 * x + 7 * y + 3 * z <= 50)
model.Add(3 * x - 5 * y + 7 * z <= 45)
model.Add(5 * x + 2 * y - 6 * z <= 37)

# It is not necessary to define an objective function
# It will return a feaseble solution anyway (If it exists)
# model.Maximize(2*x + 2*y + 3*z)

solver = cp_model.CpSolver()
status = solver.Solve(model)

print("Status = ", solver.StatusName(status))
print("OF = ", solver.ObjectiveValue())
print("x = ", solver.Value(x))
print("y = ", solver.Value(y))
print("z = ", solver.Value(z))

# To print all feaseble solutions
# Objective function must be commented

solution_printer = VarArraySolutionPrinter([x, y, z])
status = solver.SearchForAllSolutions(model, solution_printer)
