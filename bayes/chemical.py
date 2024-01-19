import graph
from core import *


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

phi=factors[1].condition(Assig({'C':1}))
print(phi)

import infer
elmi=infer.LikelihoodWeightedSampling(m=10000)

phi=bn(infer=elmi,
	   query=[C],
	   evidence=Assig({'D':1}))
print("****************")
print(phi)
