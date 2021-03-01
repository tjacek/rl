import numpy as np 

class Board(object):
	def __init__(self,true_state):
		self.true_state=true_state
		self.known_state=np.zeros(true_state.shape)

	def __str__(self):
		char=np.full(self.true_state.shape,',',dtype=str)
		char[self.true_state==2]="#"
		char= '\n'.join([''.join(row_i) 
					for row_i in char])
		return char

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
	return Board(state)

def random_ships(x=16,y=16,n_ships=(4,3,3,2)):
	ships=[]
	for size,n in enumerate(n_ships):
		size+=1
		for i in range(n):
			direction=np.random.binomial(1, p=0.5)
			if(direction):
				bounds=[x-size,y]
			else:
				bounds=[x,y-size]
			position=[np.random.randint(0, high=bound_j, dtype=int)
						for bound_j in bounds]
			ship_i=Ship(position,size,direction)
			ships.append(ship_i)
	return ships

ships=random_ships()
board=build_board(ships)
print(str(board))