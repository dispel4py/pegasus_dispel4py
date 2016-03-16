# import all necessary packages
import os,sys
parentdir = os.path.dirname(__file__)
sys.path.insert(0,parentdir)
import requests
import urllib
import urllib2
import json
from collections import defaultdict

from dispel4py.core import GenericPE
from dispel4py.workflow_graph import WorkflowGraph
from dispel4py.core import GenericPE
from dispel4py.base import ProducerPE, IterativePE, ConsumerPE
    

################################# PART 1: Create the Processing Elements  #################################
class CurlPE(ProducerPE):
    def __init__(self):
        ProducerPE.__init__(self)


    def _process(self, input):
	
	code = urllib.urlopen('http://pegasus.isi.edu')
	for i in range(10):
		self.write('output', code.readline())

class CountLinesPE(ConsumerPE):
	def __init__(self):
        	ConsumerPE.__init__(self)
		self.count = 0
	def _process(self, data):
		self.count += 1
		f = open('myfile.txt','a')
		f.write(data)
		f.close()

    

################################# PART 2: Create the PEs objects, and connect  #################################

curlPE=CurlPE()
curlPE.name="curlPE"
countLinesPE=CountLinesPE()
graph = WorkflowGraph()
graph.connect(curlPE, 'output', countLinesPE, 'input')

######################################### END ###############################################
