#!/usr/bin/env python
from DAX3 import *

# Create a DAX
dispel4py = ADAG("dispel4py")

# Add some metadata

# Add input file to the DAX-level replica catalog
#python -m dispel4py.new.processor simple pipe-countlines.py -i 10
#python -m dispel4py.new.processor simple split-countwords.py -d '{"split": [{"input": "myfile.txt"}]}'
a = File("pipe-countlines")
a.addPFN(PFN("file:///home/tutorial/dispel4py/dispel4py/examples/graph_testing/pipeline_test.py","local"))
dispel4py.addFile(a)

# Add executables to the DAX-level replica catalog
e_command1 = Executable(namespace="pipe", name="pipeline", version="4.0", os="linux", arch="x86_64", installed=True)
e_command1.addPFN(PFN("file:///home/tutorial/pegasus_dispel4py/storm_experiment/command-job.sh","local"))
dispel4py.addExecutable(e_command1)



# Add pipe-countlines job
pipe = Job(e_command1)
pipe.addArguments(a)
pipe.uses(a, link=Link.INPUT)
dispel4py.addJob(pipe)

# Add dependencies
#dispel4py.depends(parent=pipe, child=split)

# Write the DAX to stdout
import sys
dispel4py.writeXML(sys.stdout)

# Write the DAX to a file
f = open("dispel4py.dax","w")
dispel4py.writeXML(f)
f.close()
