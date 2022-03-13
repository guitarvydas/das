#!/bin/bash
# $1 is the drawio file
# $2 is the JSON file
python3 emit.py $2 `basename $1 .drawio`
