import core

class VariableElimination(object):
    def __init__(self,ordering):
        self.ordering=ordering

    def __call__(self,bn:core.BayesNet,query:list,evidence:core.Assig):
        phi = [phi_i.condition(evidence) for phi_i in bn.factors]
#        for phi_i in phi:
#            print(phi_i)
        query=set(query)
        for i in self.ordering:
            name_i = bn.variables[i].name
            if(not name_i in query):
                inds=[i for i,phi_i in enumerate(phi)
                            if(phi_i.in_scope(name_i))]
                if(len(inds)>0):
                    psi_i=core.product([phi[i] for i in inds])
                    inds=set(inds)
                    phi=[phi_i for i,phi_i in enumerate(phi)
                           if(not (i in inds))]
                    psi_i=psi_i.marginalize(name_i)
                    phi.append(psi_i)
        return core.product(phi).normalize()