import numpy as np 

class Board(object):
	def __init__(self,true_state):
		self.true_state=true_state
		self.known_state=np.zeros(true_state.shape)

class Ship(object):
	def __init__(self,position,size,direction):
		self.position=position
		self.size=size
		self.direction=direction

	def is_valid(self,dims):
		if(self.direction==0 or self.direction==1):
			if(self.direction):
				x,y=self.position[0]+self.size,self.position[1]
			else:
				x,y=self.position[0],self.position[1]+self.size
			if(x < dims[0] and y<dims[1]):
				return True 
			return False
		return False

	def __str__(self):
		x,y=self.position
		return "%d,%d,%d,%d" %(x,y,self.size,self.direction) 

def build_board(ships,x=16,y=16):
	state=np.ones((x,y))
	
	return Board(state)

ship=Ship((5,5),3,0)
print(ship.is_valid( (16,16)))