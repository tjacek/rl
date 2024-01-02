import core

class DirectSampling(object):
    def __init__(self,m=10):
        self.m=m

    def __call__(self,bn:core.BayesNet,query:list,evidence:core.Assig):
        table=core.get_factor(variables=bn.variables,
                              pairs=None)
        for i in range(self.m):
            a_i=bn.rand()       
            eq_i=[ a_i[name_j]==value_j 
                    for name_j,value_j in evidence.items()]
            if(all(eq_i)):
                b_i=a_i.select(variables=query)
                hist_i=table.get(a_i)
                table.set(a_i,hist_i+1)
        query_set=set(query)
        s_vars=[var_i for var_i in bn.variables
                  if(var_i.name in query_set)]
        factor=Factor(variables=s_vars,
                      table=table)
        return factor.normalize()

class VariableElimination(object):
    def __init__(self,ordering):
        self.ordering=ordering

    def __call__(self,bn:core.BayesNet,query:list,evidence:core.Assig):
        phi = [phi_i.condition(evidence) for phi_i in bn.factors]
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