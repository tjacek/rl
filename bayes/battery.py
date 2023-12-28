import graph
from core import *

B=Variable(name='B',
	       domian=2)
S=Variable(name='S',
	       domian=2)
E=Variable(name='E',
	       domian=2)
D=Variable(name='D',
	       domian=2)
C=Variable(name='C',
	       domian=2)
variables=[B, S, E, D, C]
factors=[get_factor(variables=[B],
	                pairs=[({'B':0},0.99),
	                       ({'B':1},0.01)]),
         get_factor(variables=[S],
	                pairs=[({'S':0},0.98),
	                       ({'S':1},0.02)]),
         get_factor(variables=[E,B,S],
	                pairs=[({'E':0,'B':0,'S':0},0.90),
	                       ({'E':0,'B':1,'S':0},0.05),
	                       ({'E':1,'B':0,'S':0},0.10),
	                       ({'E':1,'B':1,'S':0},0.95),
	                       ({'E':0,'B':0,'S':1},0.04),
	                       ({'E':0,'B':1,'S':1},0.01),
	                       ({'E':1,'B':0,'S':1},0.96),
	                       ({'E':1,'B':1,'S':1},0.99)]),
        get_factor(variables=[D,E],
	                pairs=[({'D':0,'E':0},0.96),
	                       ({'D':1,'E':0},0.04),
	                       ({'D':0,'E':1},0.03),
	                       ({'D':1,'E':1},0.97)]),
        get_factor(variables=[C,E],
	                pairs=[({'C':0,'E':0},0.98),
	                       ({'C':1,'E':0},0.02),
	                       ({'C':0,'E':1},0.01),
	                       ({'C':1,'E':1},0.99)])
        ]

g=graph.SimpleDiGraph(5)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,4)
bn=BayesNet(variables=variables,
	        factors=factors,
	        graph=g)

import infer
elmi=infer.VariableElimination([0,1,2])
phi=bn(infer=elmi,
	   query=['B'],
	   evidence=Assig({'D':1,'C':1}))
print(phi)

g.topological_sort()