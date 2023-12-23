from core import *

C=Variable(name='C',
	       domian=3)
S=Variable(name='S',
	       domian=3)
V=Variable(name='V',
	       domian=3)

p_C=get_factor(variables=[C],
	           pairs=[({'C':0},0.8),
	                  ({'C':1},0.19),
                      ({'C':2},0.01)])

p_CS=get_factor(variables=[C,S],
	              pairs=[({'C':0,'S':0},0.001),
	                     ({'C':0,'S':1},0.009),
	                     ({'C':0,'S':2},0.990),
	                     ({'C':1,'S':0},0.200),
	                     ({'C':1,'S':1},0.750),
	                     ({'C':1,'S':2},0.050),
	                     ({'C':2,'S':0},0.800),
	                     ({'C':2,'S':1},0.199),
	                     ({'C':2,'S':2},0.001)])


p_CV=get_factor(variables=[C,V],
	              pairs=[({'C':0,'V':0},0.2),
	                     ({'C':0,'V':1},0.2),
	                     ({'C':0,'V':2},0.6),
	                     ({'C':1,'V':0},0.5),
	                     ({'C':1,'V':1},0.4),
	                     ({'C':1,'V':2},0.1),
	                     ({'C':2,'V':0},0.4),
	                     ({'C':2,'V':1},0.4),
	                     ({'C':2,'V':2},0.2)])

graph=SimpleDiGraph(3)
graph.add_edge(0,1)
graph.add_edge(0,2)
bn=BayesNet(variables=[C,S,V],
	        factors=[p_C,p_CS,p_CV],
	        graph=graph)
print(bn.infer(query=['C'],
	      evidence=Assig({'S':1,'V':0})))

#import infer
#elm=infer.VariableElimination([0,1,2])
#elm.infer(bn=bn,
#	      query=['C'],
#	      evidence=Assig({'S':1,'V':0}))