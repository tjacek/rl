class Board(object):
	def __init__(self,dims,ships):
		self.dims=dims
		self.ships=ships

class Ship(object):
	def __init__(self,position,size,direction):
		self.position=position
		self.size=size
		self.direction=direction