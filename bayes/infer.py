import core

class VariableElimination(object):
    def __init__(self,ordering):
        self.ordering=ordering

    def infer(self,bn:core.BayesNet,query:list,evidence:core.Assig):
        phi = [phi_i.condition(evidence) for phi_i in bn.factors]
        for phi_i in phi:
            print(phi_i)
        query=set(query)
        for i in self.ordering:
            name_i = bn.variables[i].name
            if(not name_i in query):
                inds=[phi_i for phi_i in phi
                        if(phi_i.in_scope(name_i))]
                if(len(inds)>0):
                    product(core)