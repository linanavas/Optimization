# Ipopt does not install successfully
from pyomo.environ import *

model = ConcreteModel()

model.x = Var(initialize=1.0)
model.y = Var(initialize=1.0)

model.obj = Objective(expr=model.x**2 + model.y**2)
model.con1 = Constraint(expr=model.x**2 + model.y**2 <= 1)

opt = SolverFactory('ipopt')
results = opt.solve(model, tee=True)

model.display()