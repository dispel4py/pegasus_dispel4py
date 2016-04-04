#!/bin/bash
set -x
export PYTHON_PATH=.
export STORM_HOME=/home/tutorial/apache-storm-0.10.0
cd /home/tutorial/dispel4py
python -m dispel4py.new.processor storm dispel4py/examples/graph_testing/pipeline_test.py -m remote -i 10000
