# Optimization

This repo contains optimization examples from the Udemy course [Optimization with Python: Solve Operations Research Problems](https://www.udemy.com/course/optimization-with-python-linear-nonlinear-and-cplex-gurobi/?utm_source=adwords&utm_medium=udemyads&utm_campaign=LongTail_la.EN_cc.ROW&utm_content=deal4584&utm_term=_._ag_77879424134_._ad_535397245863_._kw__._de_c_._dm__._pl__._ti_dsa-1007766171312_._li_1003659_._pd__._&matchtype=&gclid=Cj0KCQjwldKmBhCCARIsAP-0rfyaVSAGVon-YqCde9Zk6TURDLKAe0beqpmpRje1_2pCseJ6N2FBBgoaAplkEALw_wcB)

Below find the instructions for packages installation and some notes from the course.

## Activate virtual environment

Command to create and activate virtual environment on Github codespaces: 

```
virtualenv myenv
source myenv/bin/activate
```

## Packages installation
Run ```make install```.

Use the following commands to install GLPK:
```
sudo apt update
sudo apt install glpk-utils
glpsol --version
```

This is a way to install ipopt solver for non linear problems with pyomo:

```
!wget -N -q "https://matematica.unipv.it/gualandi/solvers/ipopt-linux64.zip"
!unzip -o -q ipopt-linux64
```

## Linearization techniques

### Big M:
Binary * Continous

```
C = b*x
Where b is binary, x is continuos
Then:
-b*M <= C >= b*M
-(1-b)*M <= C-x >= (1-b)*M
```
### Two binaries:
Binary * Binary

```
C = b1 * b2
Where b1, b2 are binaries
Then:
C = z
z <= b1
z <= b2
z >= b1 + b2 - 1
z is binary
```
## Dual variables

If the dual variable of a constraint is 0, it means that the constraint is not in its boundary.  

If the dual is different than 0, it means that the constraint is in its boundary. And the dual is the "shadow price".  

Shadow prices represents how much you can improve the objective function if you "loosen/relax" the constraint a little.

## Constraint's rules in pyomo

```
model.C1 = pyo.Constraint(expr = 2*x + 2*y == 0)
model.C2 = pyo.Constraint(expr = x - 3*y >= 5)
```
Same as
```
model.C1 = pyo.Constraint(rule = myrule1)
model.C2 = pyo.Constraint(rule = myrule2)

# pyo.Constraint(RangeIndex1, RangeIndex2, ..., rule = myrule)

def myrule1(model):
    return 2*model.x + 2*model.y == 0

def myrule2(model):
    return model.x - 3*model.y >= 5
```

## Warm start with pyomo

```
model.x[0] = 1
model.x[1] = 0

...

results = opt.solve(model, warmstart = True)
```

## Other sources

Vehicle Routing problems
https://developers.google.com/optimization/routing/vrp?hl=es-419

Dynamic optimization
https://pyomo.readthedocs.io/en/stable/modeling_extensions/dae.html
