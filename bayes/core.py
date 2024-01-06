import numpy as np
import itertools

class BayesNet(object):
    def __init__(self,variables,factors,graph=None):
        self.variables=variables
        self.factors=factors
        self.graph=graph

    def __call__(self,query,evidence,infer=None):
        if(infer):
            return infer(bn=self,
                         query=query,
                         evidence=evidence)
        phi=product(self.factors)
        phi=phi.condition(evidence)
        names= list(set(phi.variable_names())-set(query))
        for name_i in names:
            phi=phi.marginalize(name=name_i)
        return phi.normalize()

    def rand(self):
        assig=Assig()
        for i in self.graph.topological_sort():
            name_i=self.variables[i].name
            phi_i=self.factors[i]
            phi_i=phi_i.condition(evidence=assig)
            assig[name_i]=phi_i.rand()[name_i]
        return assig

def product(factors):
    phi=factors[0]
    for factor_i in factors[1:]:
        phi=factor_product(phi,factor_i)
    return phi 

class Assig(dict):
    def __init__(self, arg=[]):
        super(Assig, self).__init__(arg)

    def select(self,variables):
        names= [get_name(var_i) for var_i in variables]
        return Assig({name_i:self[name_i] for name_i in names})

def get_name(var_i):
    if(type(var_i)==Variable):
        return var_i.name
    return var_i

class Variable(object):
    def __init__(self,name:str,domian:int):
        self.name=name
        self.domian=domian

    def all_values(self):
        return list(range(self.domian))

    def __str__(self):
        return self.name

class Factor(object):
    def __init__(self,variables:list,table):
        self.variables=variables
        self.table=table

    def variable_names(self):
        return [ var_i.name for var_i in self.variables]

    def in_scope(self,name):
        return any([ var_i.name==name 
                for var_i in self.variables])      

    def condition(self,evidence):
        phi=self
        for name_i,value_i in evidence.items():
            phi=phi.condition_single(name_i,value_i)
        return phi

    def condition_single(self,name,value):
        if(not self.in_scope(name)):
            return self
        pairs=[]
        for assig_i,p_i in self.table.iter():
            if(assig_i[name]==value):
                new_assig_i= assig_i.copy()
                del new_assig_i[name]
                pairs.append((new_assig_i,p_i))
        variables=[var_i for var_i in self.variables
                        if(var_i.name!=name)]
        return get_factor(variables=variables,
                          pairs=pairs)

    def marginalize(self,name:str):
        variables=[var_i for var_i in self.variables
                    if(var_i.name!=name)]
        factor_table=get_factor(variables=variables)
        for assig_i,p_i in self.table.iter():
            new_assig_i= Assig(assig_i.copy())
            del new_assig_i[name]
            p_current=factor_table.get(new_assig_i)
            factor_table.set(new_assig_i,p_current+p_i)
        return Factor(variables=variables,
                      table=factor_table)

    def normalize(self):
        z=sum([p_i for assig_i,p_i in self.table.iter()])
        for assig_i,p_i in self.table.iter():
            self.table.set(assig_i,p_i/z)
        return self

    def rand(self):
        tot,p,w=0.0,np.random.random(),self.table.sum()
        for assig_i,p_i in self.table.iter():
            tot+=(p_i/w)
            if(tot>p):
                return assig_i
        return Assig()

    def __str__(self):
        names=self.variable_names()
        s=''
        for assig_i,p_i in self.table.iter():
            desc=[ f'{name_i}={assig_i[name_i]}' 
                     for name_i in names]
            desc=','.join(desc)
            s+=f'{desc},{p_i:.6f}\n' 
        return s

class FactorTable(object):
    def __init__(self,names,array):
        self.names=names
        self.array=array
   
    def sum(self):
        return np.sum(self.array)
   
    def get(self,assig_i):
        index=self.to_index(assig_i)
        return self.array[index]

    def set(self,assig_i,p_i):
        index=self.to_index(assig_i)
        self.array[index]=p_i

    def to_index(self,assig_i):
        index=[0 for i in self.names]
        for name_i,value_i in assig_i.items():
            index[self.names[name_i]]=value_i
        return tuple(index)

    def iter(self):
        rev_names={i:name_i 
                for name_i,i in self.names.items()}
        for index, p_i in np.ndenumerate(self.array):
            assig_i={rev_names[dim_i]:value_i
                        for dim_i,value_i in enumerate(index)}
            yield Assig(assig_i),p_i

def get_factor(variables,pairs=None):
    names={var_i.name:i for i,var_i in enumerate(variables)}
    dims=tuple([var_i.domian for var_i in variables])
    array=np.zeros(dims)
    if(pairs is None):
        return FactorTable(names=names,
                           array=array)
    def helper(dict_i):
        cord= [0 for i in dims]
        for key_i,value_i in dict_i.items():
            k=names[key_i]
            cord[k]=value_i
        return tuple(cord)
    for dict_i,p_i in pairs:
        cord=helper(dict_i)
        array[cord]=p_i
    return Factor(variables=variables, 
                  table=FactorTable(names=names,
                                    array=array)) 

def all_assig(variables):
    all_values= [ [(var_i.name,value_j) 
                    for value_j in var_i.all_values()] 
                        for var_i in variables]
    return [ Assig(dict(value_i))
                for value_i in itertools.product(*all_values)]

def factor_product(phi:Factor,psi:Factor):
    phi_names=set(phi.variable_names())
    psi_names=set(psi.variable_names())
    shared = phi_names.intersection(psi_names)
    psi_only =psi_names - phi_names
    psi_only=[var_i for var_i in psi.variables
                if(var_i.name in psi_only)]
    product_variables=phi.variables +psi_only
    table=get_factor(variables=product_variables)
    for phi_assig,phi_p in phi.table.iter():
        for a_i in all_assig(psi_only):
            a_i=Assig({**phi_assig,**a_i})
            if(psi.variables):
                psi_assig=a_i.select(psi.variables)
            else:
                psi_assig=Assig()
            p_i=phi_p*psi.table.get(psi_assig)
            table.set(a_i,p_i)
    return Factor(variables=product_variables,
                  table=table)