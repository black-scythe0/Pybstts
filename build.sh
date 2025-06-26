#!/usr/bin/bash

if [ -z $1 ]; then  

python -m build

fi



if [ $1 = "clean" ]; then
    rm -rf pybstts.egg-info dist/

fi
