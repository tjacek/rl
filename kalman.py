import numpy as np

class GaussLinear(object):
	def __init__(self,state,F,H,B,Q,R):
		self.state=state
		self.F=F
		self.H=H
		self.B=B
		self.Q=Q
		self.R=R

	def act(self,u):
		self.state= self.F.dot(self.state)
		self.state+= self.B.dot(u)
		self.state+= noise(self.state,self.Q)

	def observ(self):
		v=noise(self.state,self.R)
		return self.H.dot(self.state) + v

def noise(mean,conv):
	mean=np.zeros_like(mean)
	return np.random.multivariate_normal(mean,conv)

def simple_model():
	F=[[0,np.sqrt(2),1],
	    [1,-1,4],
	    [2,0,1]]
	B=[[1,0],
	   [0,1],
	   [1,1]]
	Q,R,H=np.identity(3),np.identity(3),np.identity(3)
	F,B=np.array(F),np.array(B)
	state=np.ones(3)
	gs=GaussLinear(state,F,H,B,Q,R)
	return gs

gs=simple_model()
print(gs.act(np.ones(2).T))
print(gs.observ())