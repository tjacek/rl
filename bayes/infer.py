import core

class VariableElimination(object):
    def __init__(self,ordering):
        self.ordering=ordering

    def infer(bn:core.BayesNet,query:list,evidence:core.Assig):
    	phi = [phi_i.condition(evidence) for phi_i in bn.factors]
        for i in self.ordering
            name_i = bn.variables[i].name