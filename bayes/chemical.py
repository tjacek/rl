import matplotlib.pyplot as plt
import graph,infer
from core import *

def get_algs(m_samples:int):
    algs={'like' :infer.LikelihoodWeightedSampling(m=m_samples),
          'gibbs':infer.GibbsSampling(m_samples=m_samples,
	                          m_burnin=100,
	                          m_skip=100,
	                          ordering=[0,1])}
    return algs

def plot(bn,query,evidence,step=125,n_steps=10):
    samples=np.arange(n_steps)*step
    var_name=query[0].name
    ts_series={'like':[],'gibbs':[]}
    for sample_i in samples:
    	print(f'n_samples:{sample_i}')
    	for name_j,alg_j in get_algs(sample_i).items():
            dist_j=bn(infer=alg_j,
                      query=query,
    	              evidence=evidence)
            value_i= dist_j.table.get({var_name:1})
            if(np.isnan(value_i)):
            	print(value_i)
            	value_i=0.0
            ts_series[name_j].append(value_i)
    print(ts_series)
    for name_i,y_i in ts_series.items():
        plt.plot(samples,y_i , 
        	     label=name_i, 
                 linewidth=3)
    plt.legend()
    plt.tight_layout()
    plt.show()

C=Variable(name='C',
	       domian=2)
D=Variable(name='D',
	       domian=2)

variables=[C, D]
factors=[get_factor(variables=[C],
	                pairs=[({'C':0},0.999),
	                       ({'C':1},0.001)]),
         get_factor(variables=[C,D],
	                pairs=[({'C':0,'D':0},0.999),
	                       ({'C':1,'D':0},0.001),
	                       ({'C':0,'D':1},0.001),
	                       ({'C':1,'D':1},0.999)])]

g=graph.SimpleDiGraph(2)
g.add_edge(0,1)
bn=BayesNet(variables=variables,
	        factors=factors,
	        graph=g)

#phi=factors[1].condition(Assig({'C':1}))
#print(phi)


#phi=bn(infer=alg,
#	   query=[C],
#	   evidence=Assig({'D':1}))

plot(bn=bn,
	 query=[C],
     evidence=Assig({'D':1}))
#print("****************")
#print(phi)