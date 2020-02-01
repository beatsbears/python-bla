#!/bin/bash

# Run python script & capture pid
python vulnerable.py &
export PYTHON_PID=$!

# Report on memory use for as long as we can
for (( c=1; c<=20; c++ ))
do  
    KB=$(pmap -x $PYTHON_PID | tail -n 1 | awk '{ print $3 }')
    echo "Using: $KB Kb"
    sleep 1
done