import numpy as np#,random
from enum import Enum

class InnerStates(Enum):
	HUNGRY=0
	SATED=1

class Observations(Enum):
	CRYING=0 
	QUIET=1

class Actions(Enum):
	FEED=0
	SING=1
	IGNORE=2

class CryingBaby(object):
	def __init__(self):
		self.state=InnerStates.SATED
		self.last_action=Actions.IGNORE
		prob=[[0.8,0.9,0.8],
			  [0.1,0.0,0.1]]
		self.prob=np.array(prob)

	def get_states(self):
		return list(Observations)

	def get_actions(self):
		return list(Actions)

	def observe(self):
		x,y=self.state.value,self.last_action.value
		p_as=self.prob[x,y]
		return np.random.choice(self.get_states(), p=[p_as,1.0-p_as])

#	def act(self,action_i):


baby=CryingBaby()
print(baby.observe())