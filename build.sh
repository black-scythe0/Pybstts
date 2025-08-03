#!/usr/bin/bash

if [ $1 = "--clean-cache" ]; then
    rm -rf pybstts/__pycache__/;
    rm -rf pybstts/tts/__pycache__/;

fi

if [ -z $1 ]; then  

    python -m build

fi



if [ $1 = "--clean" ]; then
    rm -rf pybstts.egg-info dist/

fi


if [ $1 = "--publish" ]; then
    twine upload --repository testpypi dist/*
    
fi
