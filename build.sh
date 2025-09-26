#!/usr/bin/bash


case $1 in
    --clean-cache)
        rm -rf pybstts/__pycache__/;
        rm -rf pybstts/tts/__pycache__/;
    ;;

    --clean) 
        rm -rf pybstts.egg-info dist/
    ;;
    
    --publish)
        twine upload --repository testpypi dist/*
    ;;

    *)
        python3 -m build
    ;;
esac
