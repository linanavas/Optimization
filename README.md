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

Use the following commands to install IPOPT
```
sudo apt-get update
sudo apt-get install gfortran pkg-config
sudo apt-get install liblapack-dev

wget https://github.com/coin-or/Ipopt/archive/refs/tags/releases/x.x.x.tar.gz
tar -xzf x.x.x.tar.gz

cd Ipopt-releases-x.x.x  # Replace x.x.x with the version you downloaded
./configure
make
sudo make install
```

Check the latest version (x.x.x) in https://github.com/coin-or/Ipopt/releases