#!/bin/bash
make -C ../
cp ../push_swap ./bin/
python3 main.py $1 $2