# Optimization

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

This is a way to install ipopt solver for non linear problems with pyomo

```
!wget -N -q "https://matematica.unipv.it/gualandi/solvers/ipopt-linux64.zip"
!unzip -o -q ipopt-linux64
```