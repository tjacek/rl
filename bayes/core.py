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
   
class BayesNet(object):
    def __init__(self,variables,factors,graph=None):
        if(graph is None):
            graph=SimpleDiGraph(len(variables))
        self.variables=variables
        self.factors=factors
        self.graph=graph

class Variable(object):
	def __init__(self,name:str,domian:int):
		self.name=name
		self.domian=domian

class Factor(object):
    def __init__(self,variables:list,table):
        self.variables=variables
        self.table=table

    def variable_names(self):
        return [var_i.name for var_i in self.variables]

    def in_scope(self,name):
        return any([ var_i.name==name 
                for var_i in self.variables])      

    def condition(self,name,value):
        if(not select.in_scope(name)):
            return self
        pairs=[]
        for assig_i,p_i in self.table.iter():
            if(assig_i[name]==value):
                pairs.append((assig_i,p_i))
        vars=[var_i for var_i in self.variables
                if(var_i.name==name)]

    def __str__(self):
        names=self.variable_names()
        s=''
        for assig_i,p_i in self.table.iter():
            desc=[ f'{name_i}={assig_i[name_i]}' 
                     for name_i in names]
            desc=','.join(desc)
            s+=f'{desc},{p_i}\n' 
        return s

class FactorTable(object):
    def __init__(self,names,array):
        self.names=names
        self.array=array

    def iter(self):
        rev_names={i:name_i 
                for name_i,i in self.names.items()}
        for index, p_i in np.ndenumerate(self.array):
            assig_i={rev_names[dim_i]:value_i
                        for dim_i,value_i in enumerate(index)}
            yield Assig(assig_i),p_i
    
    def marginalize(self,name_i:str):
        i=self.names[name_i]
        return np.sum(self.array,axis=i)

def get_factor(variables,pairs):
    names={var_i.name:i for i,var_i in enumerate(variables)}
    dims=tuple([var_i.domian for var_i in variables])
    array=np.zeros(dims)
    def helper(dict_i):
        cord= [0 for i in dims]
        for key_i,value_i in names.items():
            k=names[key_i]
            cord[k]=value_i
        return tuple(cord)
    for dict_i,p_i in pairs:
        cord=helper(dict_i)
        array[cord]=p_i
    return Factor(variables=variables, 
                  table=FactorTable(names=names,
                                    array=array)) 


def factor_product(phi:Factor,psi:Factor):
    phi_names=phi.variable_names()
    phi_names=phi.variable_names()
#    FactorTable(object)