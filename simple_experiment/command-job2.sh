#!/bin/bash
scl enable python27 "python -m dispel4py.new.processor simple $1 -d '{\"split\": [{\"input\": \"$2\"}]}'"
