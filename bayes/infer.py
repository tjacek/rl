import core

class DirectSampling(object):
    def __init__(self,m=10):
        self.m=m

    def __call__(self,bn:core.BayesNet,query:list,evidence:core.Assig):
        query_set=set([var_i.name for var_i in query])
        s_vars=[var_i for var_i in bn.variables
                  if(var_i.name in query_set)]
        table=core.get_factor(variables=s_vars,
                              pairs=None)
        for i in range(self.m):
            a_i=bn.rand()       
            eq_i=[ a_i[name_j]==value_j 
                    for name_j,value_j in evidence.items()]
            if(all(eq_i)):
                t_i=a_i.select(variables=query)
                hist_i=table.get(t_i)
                table.set(t_i,hist_i+1)
            b_i=a_i.select(variables=query)
            hist_i=table.get(b_i)
            table.set(b_i,hist_i+1)
        factor=core.Factor(variables=s_vars,
                           table=table)
        return factor.normalize()

class LikelihoodWeightedSampling(object):
    def __init__(self,m=10):
        self.m=m

    def __call__(self,bn:core.BayesNet,query:list,evidence:core.Assig):
        ordering = bn.graph.topological_sort()
        query_set=set([var_i.name for var_i in query])
        s_vars=[var_i for var_i in bn.variables
                  if(var_i.name in query_set)]
        table=core.get_factor(variables=s_vars,
                              pairs=None)
        for i in range(self.m):
            a_i,w_i=bn.rand(),1.0
            for j in ordering:
                name_j=bn.variables[j].name
                phi_j=bn.factors[j]
                if(name_j in evidence):
                    a_i[name_j]=evidence[name_j]
                    b_j=a_i.select(phi_j.variables) #_names())
                    w_i*= phi_j.table.get(a_i.select(b_j))
                else:
                    phi_j.condition(a_i)
                    a_i[name_j]=phi_j.rand()[name_j]
            b_i=a_i.select(variables=query)
            hist_i=table.get(b_i)
            table.set(b_i,hist_i+w_i)
        factor=core.Factor(variables=s_vars,
                           table=table)
        return factor.normalize()

    def get_weight(self,bn,a_i,evidence):
        w_i=1.0
        ordering = bn.graph.topological_sort()
        for j in ordering:
            name_j=bn.variables[j].name
            phi_j=bn.factors[j]
            if(name_j in evidence):
                b_j=a_i.select(phi_j.variables) #_names())
                w_i*= phi_j.table.get(a_i.select(b_j))
            else:
                phi_j.condition(a_i)
                a_i[name_j]=phi_j.rand()[name_j]
        return w_i

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