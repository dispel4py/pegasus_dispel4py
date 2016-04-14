#!/bin/bash
set -x
export PYTHON_PATH=.
cd /home/tutorial/dispel4py

export DISPEL4PY_XCORR_STARTTIME=2015-04-06T06:00:00.000
export DISPEL4PY_XCORR_ENDTIME=2015-04-06T07:00:00.000

#dispel4py multi realtime_xcorr.py -n 4
python -m dispel4py.new.processor multi tc_cross_correlation/realtime_xcorr.py -n 4 
