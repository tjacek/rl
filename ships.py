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

	def end_point(self):
		if(self.direction):
				return self.position[0]+self.size,self.position[1]
		return self.position[0],self.position[1]+self.size

	def is_valid(self,dims):
		if(self.direction==0 or self.direction==1):
			x,y=self.end_point()
			if(x < dims[0] and y<dims[1]):
				return True 
			return False
		return False

	def __str__(self):
		x,y=self.position
		return "%d,%d,%d,%d" %(x,y,self.size,self.direction) 

def build_board(ships,x=16,y=16):
	state=np.ones((x,y))
	for ship_i in ships:
		if(not ship_i.is_valid(state.shape)):
			raise Exception("Ships invalid %s" % str(ship_i))
		start_i=ship_i.position
		end_i=ship_i.end_point()
		if(ship_i.direction):
			state[start_i[0]:end_i[0],start_i[0]]=2
		else:
			state[start_i[0],start_i[1]:end_i[1]]=2
			
		print(start_i)
		print(end_i)
	return Board(state)

ships=[Ship((5,5),3,0),Ship((3,8),2,0),Ship((9,9),4,1)]
board=build_board(ships)
print(board.true_state)
#print(ship.is_valid( (16,16)))