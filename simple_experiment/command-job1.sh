#!/bin/bash
set -x
scl enable python27 "dispel4py simple $1 -i 10"
