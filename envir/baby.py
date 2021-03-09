import numpy as np
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
		return len(Observations) #range(len(Observations))

	def get_actions(self):
		return len(Actions)#range(len(Actions))

	def observe(self):
		x,y=self.state.value,self.last_action.value		
		p_as=self.prob[x,y]
		if(np.random.uniform()<p_as):
			return Observations.CRYING.value
		return Observations.QUIET.value

	def act(self,action_i):
		if(np.issubdtype(type(action_i),np.integer)):
			action_i=Actions(action_i)
		if(self.state==InnerStates.HUNGRY):
			if(action_i==Actions.FEED):
				self.state=InnerStates.SATED
		else:
			if(action_i!=Actions.FEED):
				if(np.random.uniform()<0.1):
					self.state=InnerStates.HUNGRY
		self.last_action=action_i
		return self.compute_reward(action_i)

	def compute_reward(self,action_i):
		reward=0.0
		if(self.state==InnerStates.HUNGRY):
			reward-=10
		if(action_i==Actions.FEED):
			reward-=5
		if(action_i==Actions.SING):
			reward-=0.5
		return reward

	def reset(self):
		self.state=InnerStates.SATED
		self.last_action=Actions.IGNORE
		
if __name__ == "__main__":
	baby=CryingBaby()
	print(baby.act(Actions.IGNORE))