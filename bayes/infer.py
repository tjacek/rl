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
            a_i,w_i=core.Assig(),1.0
            for j in ordering:
                name_j=bn.variables[j].name
                phi_j=bn.factors[j]
                if(name_j in evidence):
                    a_i[name_j]=evidence[name_j]
                    t_j=a_i.select(phi_j.variables) 
                    w_i*= phi_j.table.get(t_j)
                else:
                    phi_j.condition(a_i)
                    a_i[name_j]=phi_j.rand()[name_j]
            print(a_i)
            b_i=a_i.select(variables=query)
            hist_i=table.get(b_i)
            table.set(b_i,hist_i+w_i)
        factor=core.Factor(variables=s_vars,
                           table=table)
        return factor.normalize()

class GibbsSampling(object):
    def __init__(self,m_samples:int,m_burnin:int,m_skip:int,ordering:list):
        self.m_samples=m_samples
        self.m_burnin=m_burnin
        self.m_skip=m_skip
        self.ordering=ordering

    def __call__(self,bn:core.BayesNet,query:list,evidence:core.Assig):
        table=core.get_factor(variables=bn.variables,
                              pairs=None)
        a=bn.rand()
        a=core.Assig({name_i:value_i 
                        for name_i,value_i in a.items()
                            if(not name_i in evidence)})
        a=self.gibbs_sample(a,bn, evidence)
        for i in range(self.m_samples):
            a=self.gibbs_sample(a,bn, evidence)


    def gibbs_sample(self,a:core.Assig,bn:core.BayesNet, evidence:core.Assig):
        for j in range(self.m_skip):
            a=self.update_gibbs_sample(a, bn,evidence)
        return a

    def update_gibbs_sample(self,a:core.Assig,bn:core.BayesNet, evidence:core.Assig):
        for i in self.ordering:
            name_i=bn.variables[i].name
            if(not name_i in evidence):
                b=bn.blanket(a,i)
                a[name_i]=b.rand()[name_i]
        return a

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