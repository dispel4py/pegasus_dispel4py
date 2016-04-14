#!/bin/bash
set -x
export PYTHON_PATH=.
cd /home/tutorial/dispel4py

export DISPEL4PY_XCORR_STARTTIME=2015-04-06T06:00:00.000
export DISPEL4PY_XCORR_ENDTIME=2015-04-06T07:00:00.000

rm -rf /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/DATA
rm -rf /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/XCORR

mkdir /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/DATA
mkdir /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/XCORR


#dispel4py multi tc_cross_correlation/realtime_prep.py -f tc_cross_correlation/realtime_xcorr_input.jsn -n 4	
python -m dispel4py.new.processor multi tc_cross_correlation/realtime_prep.py -f tc_cross_correlation/realtime_xcorr_input.jsn -n 4

