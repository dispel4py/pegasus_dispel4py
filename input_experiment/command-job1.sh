#!/bin/bash
set -x
scl enable python27 "dispel4py multi $1 -n 4 -d '{\"curlPE\": [{\"input\": \"$2\"}]}'"
