class rectangle:
	length = None
	breadth = None
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def Area(self):
		return self.length*self.breadth
	def Perimeter(self):
		return 2*(self.length+self.breadth)
	def isSquare(self):
		if(self.length == self.breadth):
			return True
		else:
			return False
	def length(self):
		return self.length
	def breadth(self):
		return self.breadth
robj = rectangle(10,4)
print(robj.Area())
print(robj.Perimeter())
print(robj.isSquare())