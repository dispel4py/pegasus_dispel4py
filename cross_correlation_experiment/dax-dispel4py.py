#!/usr/bin/env python
from DAX3 import *

# Create a DAX
dispel4py = ADAG("dispel4py")

# Add some metadata

# Add input file to the DAX-level replica catalog
#python -m dispel4py.new.processor simple pipe-countlines.py -i 10
#python -m dispel4py.new.processor simple split-countwords.py -d '{"split": [{"input": "myfile.txt"}]}'

e_command1 = Executable(namespace="cross_correlation", name="pre_cross", version="4.0", os="linux", arch="x86_64", installed=True)
e_command1.addPFN(PFN("file:///home/tutorial/pegasus_dispel4py/cross_correlation_experiment/command-job1.sh","local"))
dispel4py.addExecutable(e_command1)


e_command2 = Executable(namespace="cross_correlation", name="post_cross", version="4.0", os="linux", arch="x86_64", installed=True)
e_command2.addPFN(PFN("file:///home/tutorial/pegasus_dispel4py/cross_correlation_experiment/command-job2.sh","local"))
dispel4py.addExecutable(e_command2)

# Add pipe-countlines job
preprocess = Job(e_command1)
b1 = File("preprocess_data.zip")
preprocess.uses(b1, link=Link.OUTPUT, transfer=True)
dispel4py.addJob(preprocess)


postprocess = Job(e_command2)
postprocess.uses(b1, link=Link.INPUT)
dispel4py.addJob(postprocess)


# Add dependencies
dispel4py.depends(parent=preprocess, child=postprocess)

# Write the DAX to stdout
import sys
dispel4py.writeXML(sys.stdout)

# Write the DAX to a file
f = open("dispel4py.dax","w")
dispel4py.writeXML(f)
f.close()
