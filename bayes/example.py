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
vars=[B, S, E, D, C]

#factors=[get_factor(variables=[D,E],
#	                pairs=[({'D':0,'E':0},0.96),
#	                       ({'D':0,'E':1},0.03),
#	                       ({'D':1,'E':0},0.04),
#	                       ({'D':1,'E':1},0.97)])]

#get_factor(variables=[B],
#	                pairs=[({'B':0},0.99),
#	                       ({'B':1},0.01)])]

#graph=SimpleDiGraph(5)
#graph.add_edge(1,3)
#graph.add_edge(2,3)
#graph.add_edge(3,4)
#graph.add_edge(3,5)
#bn=BayesNet(variables=vars,
#	        factors=factors,
#	        graph=graph)

X=Variable(name='X',
	       domian=2)
Y=Variable(name='Y',
	       domian=2)
Z=Variable(name='Z',
	       domian=2)

factor=get_factor(variables=[X,Y,Z],
	              pairs=[({'X':0,'Y':0,'Z':0},0.08),
	                     ({'X':0,'Y':0,'Z':1},0.31),
	                     ({'X':0,'Y':1,'Z':0},0.09),
	                     ({'X':0,'Y':1,'Z':1},0.37),
	                     ({'X':1,'Y':0,'Z':0},0.01),
	                     ({'X':1,'Y':0,'Z':1},0.05),
	                     ({'X':1,'Y':1,'Z':0},0.02),
	                     ({'X':1,'Y':1,'Z':1},0.07), ])

print(factor)
print(factor.marginalize('Y'))