#!/bin/bash

# FILE: test_MathLib.sh
# DATE: 2 JAN 2023
# AUTH: G. E. Deschaines
# PROG: Shell script invoked in ./tests subdirectory of cartwheel-3d home directory.
# DESC: Builds and executes test_MathLib.exe, a C++ program to exercise various 
#       MathLib library components such as implementation of Pythonized Vector3d
#       element indexing.

INCS="-I${CW3D_HOME} -I{CW3D_HOME}/Utils -I{CW3D_HOME}/MathLib"
LIBS="-L${CW3D_HOME}/lib/Debug -l_Utils -l_MathLib"

# Build test_MathLib.exe
gcc -O0 -std=c++11 -fpermissive ${INCS} -o test_MathLib.exe test_MathLib.cpp ${LIBS} -lstdc++

# Execute test_MathLib.exe
LD_LIBRARY_PATH=${CW3D_HOME}/lib/Debug:$LD_LIBRARY_PATH; ./test_MathLib.exe
