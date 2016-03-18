#!/bin/bash
scl enable python27 "dispel4py simple $1 -d '{\"split\": [{\"input\": \"$2\"}]}'"
