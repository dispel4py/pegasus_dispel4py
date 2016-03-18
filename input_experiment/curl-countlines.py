import requests
import urllib

from dispel4py.workflow_graph import WorkflowGraph
from dispel4py.base import ProducerPE, ConsumerPE


################################# PART 1: Create the Processing Elements  #################################
class CurlPE(ProducerPE):
    def __init__(self):
        ProducerPE.__init__(self)


    def _process(self, inputs):
        with open(inputs['input']) as f:
            for line in f:
                code = urllib.urlopen(line)
                for i in range(10):
                    self.write('output', code.readline())

class CountLinesPE(ConsumerPE):
    def __init__(self):
        ConsumerPE.__init__(self)
        self.count = 0
    def _process(self, data):
        self.count += 1
        with open('myfile.txt','a') as f:
            f.write(data)



################################# PART 2: Create the PEs objects, and connect  #################################

curlPE=CurlPE()
curlPE.name="curlPE"
countLinesPE=CountLinesPE()
graph = WorkflowGraph()
graph.connect(curlPE, 'output', countLinesPE, 'input')

######################################### END ###############################################
