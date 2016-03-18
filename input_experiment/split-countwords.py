from collections import defaultdict

from dispel4py.workflow_graph import WorkflowGraph
from dispel4py.core import GenericPE
from dispel4py.base import ProducerPE
    

################################# PART 1: Create the Processing Elements  #################################
class SplitWordsPE(ProducerPE):

    def __init__(self):
        ProducerPE.__init__(self)
        
    def _process(self, inputs):
	with open(inputs['input']) as f:
            for word in f.read().split():
                self.write("output", (word,1))

class CountWordsPE(GenericPE):
    def __init__(self):
        GenericPE.__init__(self)
        self._add_input("input", grouping=[0])
        self._add_output("output")
        self.count=defaultdict(int)
        
    def _process(self, inputs):
        word, count = inputs['input']
        self.count[word] += count
    
    def _postprocess(self):
        self.write('output', self.count)
    

################################# PART 2: Create the PEs objects, and connect  #################################

splitPE=SplitWordsPE()
splitPE.name = "split"
countWordsPE= CountWordsPE()
graph = WorkflowGraph()
graph.connect(splitPE, 'output', countWordsPE, 'input')

######################################### END ###############################################
