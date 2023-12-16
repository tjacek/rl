from core import *

X=Variable(name='X',
	       domian=2)
Y=Variable(name='Y',
	       domian=2)
Z=Variable(name='Z',
	       domian=2)

def marg_test():
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

phi=get_factor(variables=[X,Y],
	              pairs=[({'X':0,'Y':0},0.3),
	                     ({'X':0,'Y':1},0.4),
	                     ({'X':1,'Y':0},0.2),
	                     ({'X':1,'Y':1},0.1)])

psi=get_factor(variables=[Y,Z],
	              pairs=[({'Y':0,'Z':0},0.2),
	                     ({'Y':0,'Z':1},0.0),
	                     ({'Y':1,'Z':0},0.3),
	                     ({'Y':1,'Z':1},0.5)])

#all_assig(phi1.variables)
product= factor_product(phi,psi)
print(product)