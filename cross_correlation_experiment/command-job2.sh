#!/bin/bash
set -x
export PYTHON_PATH=.
export STORM_HOME=/home/tutorial/apache-storm-0.10.0


rm -rf /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/DATA/
rm -rf /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/XCORR/


mkdir -p /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/DATA/
mkdir -p /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/XCORR/

cp `pwd`/preprocess_data.zip /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/DATA/
cd /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/DATA/
unzip preprocess_data.zip

rm -rf /home/tutorial/dispel4py/tc_cross_correlation/OUTPUT/DATA/preprocess_data.zip

cp -r /home/tutorial/dispel4py/tc_cross_correlation/  /home/tutorial/dispel4py/resources/.


cd /home/tutorial/dispel4py

python -m dispel4py.new.processor storm tc_cross_correlation/realtime_xcorr_storm.py -m remote 
