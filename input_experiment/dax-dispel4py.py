#!/usr/bin/env python
from DAX3 import *

# Create a DAX
dispel4py = ADAG("dispel4py")

# Add some metadata

# Add input file to the DAX-level replica catalog
#python -m dispel4py.new.processor simple curl-countlines.py -i 10
#python -m dispel4py.new.processor simple split-countwords.py -d '{"split": [{"input": "myfile.txt"}]}'
a = File("curl-countlines")
a.addPFN(PFN("file:///home/tutorial/pegasus_dispel4py/input_experiment/curl-countlines.py","local"))
dispel4py.addFile(a)

a1 = File("myinput")
a1.addPFN(PFN("file:///home/tutorial/pegasus_dispel4py/input_experiment/myinput.txt","local"))
dispel4py.addFile(a1)

b = File("split-countwords")
b.addPFN(PFN("file:///home/tutorial/pegasus_dispel4py/input_experiment/split-countwords.py","local"))
dispel4py.addFile(b)

# Add executables to the DAX-level replica catalog
e_command1 = Executable(namespace="curl", name="curlcount", version="4.0", os="linux", arch="x86_64", installed=True)
e_command1.addPFN(PFN("file:///home/tutorial/command-job1.sh","local"))
dispel4py.addExecutable(e_command1)

e_command2 = Executable(namespace="curl", name="splitcount", version="4.0", os="linux", arch="x86_64", installed=True)
e_command2.addPFN(PFN("file:///home/tutorial/command-job2.sh","local"))
dispel4py.addExecutable(e_command2)


# Add curl-countlines job
curl = Job(e_command1)
b1 = File("myfile.txt")
curl.addArguments(a,a1)
curl.uses(a, link=Link.INPUT)
curl.uses(a1, link=Link.INPUT)
curl.uses(b1, link=Link.OUTPUT, transfer=True)
dispel4py.addJob(curl)

# Add split-countwords job
split = Job(e_command2)
split.addArguments(b,b1)
split.uses(b, link=Link.INPUT)
split.uses(b1, link=Link.INPUT)
dispel4py.addJob(split)

# Add dependencies
dispel4py.depends(parent=curl, child=split)

# Write the DAX to stdout
import sys
dispel4py.writeXML(sys.stdout)

# Write the DAX to a file
f = open("dispel4py.dax","w")
dispel4py.writeXML(f)
f.close()
