#!/bin/bash
set -x
scl enable python27 "python -m dispel4py.new.processor simple $1 -i 10"
