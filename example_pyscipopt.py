# It is necessary to install the package using a website

from pyscipopt import Model

model = Model('example')

#Linear and non linear problems
#Does not enable comercial solvers

x = model.addVar('x')
y = model.addVar('y')

model.setObjective(x+y, sense = 'maximize')

model.addCons(-x+2*y<=8)
model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)

model.optimize()

sol = model.getBestSol()

print('x=',sol[x])
print('y=',sol[y])