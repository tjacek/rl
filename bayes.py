import numpy as np

class Assig(dict):
    def __init__(self, arg=[]):
        super(Assig, self).__init__(arg)

    def select(self,variables):
    	return Assig({var_i.name:self[var_i.name]
    		        for var_i in variables})

class SimpleDiGraph(object):
    def __init__(self,n_nodes:int):
        self.near=[[] for i in range(n_nodes)]

    def add_edge(self,start,end):
        self.near[start].append(end)
   
class BayesNets(object):
    def __init__(self,variables,graph=None):
    	if(graph is None):
    		graph=SimpleDiGraph(len(variables))
        self.variables=variables
        self.graph=graph

class Variable(object):
	def __init__(self,name:str,domian:str):
		self.name=name
		self.domian=domian

class Factor(object):
    def __init__(self,variables:list,table):
        self.variables=variables
        self.table=table

    def variable_names(self):
        return [var_i.name for var_i in self.variables]


X=Variable(name='X', 
	       domian=2)
Y=Variable(name='Y', 
	       domian=2)
Z=Variable(name='X', 
	       domian=2)

table=np.zeros((2,2,2))
table[0][0][0]=0.08
table[0][1][0]=0.09
table[1][0][0]=0.01
table[1][1][0]=0.02
table[0][0][1]=0.31
table[0][1][1]=0.37
table[1][0][1]=0.05
table[1][1][1]=0.07
Factor(variables=[X,Y.Z],
	   table=table)