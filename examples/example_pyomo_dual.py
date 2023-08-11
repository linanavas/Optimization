import pyomo.environ as pyo, ipdb
from pyomo.opt import SolverFactory

# creating the model
m = pyo.ConcreteModel()

# parameters
C1 = 100
C2 = 300
Nmax1 = 30
Nmax2 = 100
D = 50

# variables
m.N1 = pyo.Var()
m.N2 = pyo.Var()
N1 = m.N1
N2 = m.N2

# objective function and constraints
m.obj = pyo.Objective(expr=C1 * N1 + C2 * N2)
m.C1 = pyo.Constraint(expr=N1 + N2 == D)
m.C2 = pyo.Constraint(expr=N1 <= Nmax1)
m.C3 = pyo.Constraint(expr=N2 <= Nmax2)

# solving model
m.dual = pyo.Suffix(direction=pyo.Suffix.IMPORT)
opt = SolverFactory("glpk")
m.results = opt.solve(m)

# prints the model
print("-" * 20 + " MODEL " + "-" * 20)
m.pprint()

# prints the dual variables
print("\n\n" + "-" * 20 + " DUAL VARIABLES " + "-" * 20)
m.dual.pprint()

# prints the objective function
print("\n\n" + "-" * 20 + " Value of ObjFun " + "-" * 20)
print("Objective Function is %.2f" % (pyo.value(m.obj)))

# access a single dual variable
print("\n\n" + "-" * 20 + " Value of a single dual variable " + "-" * 20)
mydual = m.dual[m.C2]
print("C2 dual is %.2f" % (mydual))

# access slack of a constraint
print("\n\n" + "-" * 20 + " Value of slacks " + "-" * 20)
upper_slack = m.C3.uslack()
lower_slack = m.C3.lslack()
print("Upper slack = %.2f" % (upper_slack))
print("Lower slack = %.2f" % (lower_slack))
