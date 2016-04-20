# Get to stage where all is xc-d tehn append a new taskfarm according to what 
# is to be done with the xc's.
# and look at inputs['input'] from the shm in memory files.

from dispel4py.core import GenericPE 
from dispel4py.workflow_graph import WorkflowGraph
from dispel4py.base import BasePE, IterativePE, ConsumerPE, create_iterative_chain

import numpy as np
import time
import os, shutil
import traceback
from tc_cross_correlation.xcorr import xcorrf, xcorrf_noFFT 
from  distutils.dir_util  import create_tree as mkadir
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.backends
from obspy import read

ROOT_DIR = './tc_cross_correlation/OUTPUT/'
starttime='2015-04-06T06:00:00.000'
             
class Product(GenericPE):
    def __init__(self):
        GenericPE.__init__(self)
	self._add_output('output', tuple_type=['number', 'index', 'store', 'string'])
    def process(self, inputs):
        store = []
        for dir in os.listdir(ROOT_DIR + 'DATA/'+ starttime):
	    for f in os.listdir(ROOT_DIR+'/DATA/'+ starttime +'/'+ dir):
	       file=ROOT_DIR+'DATA/'+ starttime + '/'+ dir+'/'+f
               str1=np.load(file)
               index = len(store)
               for i in range(index):
                  self.write('output',[i, index, store[i], str1])
               #self.log('The station %s is index %s' %(f,index))	
               store.append(str1)

class Xcorr(GenericPE):
    def __init__(self):
        GenericPE.__init__(self)
	self._add_input('input')
	self._add_output('output', tuple_type=['number', 'index', 'xcorr'])
    def process(self, inputs):
	self.log('Xcorr inputs are %s' % inputs['input'])
        str1=inputs['input'][2]
        str2=inputs['input'][3]
	try:
            xcorr1 = xcorrf_noFFT(str1, str2, 5000)
            self.write('output',[inputs['input'][0], inputs['input'][1], xcorr1])
        except:
	    self.log('error in %s_%s xcorr' % (inputs['input'][0], inputs['input'][1]))
            self.log(traceback.format_exc())


class StoreToFile(GenericPE):
    def __init__(self, filename):
        GenericPE.__init__(self)
	self._add_input('input')
        self.filename = filename
	self.counter = 0
    def process(self, inputs):
        xcorr1 = inputs['input'][2]
	directory=ROOT_DIR+'XCORR/'+starttime+'/'+str(inputs['input'][0])+'_'+str(inputs['input'][1])
	if not os.path.exists(directory):
    	    os.makedirs(directory)
        fout = directory+'/%s_%s_%s.out' % (self.filename, inputs['input'][0], inputs['input'][1])
        np.save(fout, xcorr1)
	self.counter += 1
	


class Plot(GenericPE):
    def __init__(self, filename):
        GenericPE.__init__(self)
	self._add_input('input')
        self.filename = filename
    def process(self, inputs):
	xcorr1 = inputs['input'][2]
        fout = ROOT_DIR+'XCORR/%s_%s_%s.plot.png' % (self.filename, inputs['input'][0], inputs['input'][1])
        sps=4
        plt.plot(np.linspace((-len(xcorr1)+1)/(2*sps),len(xcorr1)/(2*sps),len(xcorr1)), xcorr1)
        plt.xlim(-1000,1000)
        plt.savefig(fout)


graph = WorkflowGraph()
product=Product()
xcorr1=Xcorr()
store=StoreToFile('Xcorr')
plot = Plot('Xcorr')
graph.connect(product, 'output', xcorr1, 'input')
graph.connect(xcorr1, 'output', store, 'input')
graph.connect(xcorr1, 'output', plot, 'input')

