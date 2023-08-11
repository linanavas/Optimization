# Optimization

This repo contains optimization examples from the Udemy course [Optimization with Python: Solve Operations Research Problems](https://www.udemy.com/course/optimization-with-python-linear-nonlinear-and-cplex-gurobi/?utm_source=adwords&utm_medium=udemyads&utm_campaign=LongTail_la.EN_cc.ROW&utm_content=deal4584&utm_term=_._ag_77879424134_._ad_535397245863_._kw__._de_c_._dm__._pl__._ti_dsa-1007766171312_._li_1003659_._pd__._&matchtype=&gclid=Cj0KCQjwldKmBhCCARIsAP-0rfyaVSAGVon-YqCde9Zk6TURDLKAe0beqpmpRje1_2pCseJ6N2FBBgoaAplkEALw_wcB)

Below find some notes and instructions for packages installation.


Use the following commands to install GLPK:
```
sudo apt update
sudo apt install glpk-utils
glpsol --version
```

Command to create and activate virutal environment: 

```
virtualenv myenv
source myenv/bin/activate
```

## Packages installation

This is a way to install ipopt solver for non linear problems with pyomo

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
=====>
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

## Other sources

Vehicle Routing problems
https://developers.google.com/optimization/routing/vrp?hl=es-419