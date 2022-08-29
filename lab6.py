class complex:
	# real =None
	# img = None
	def __init__(self,real,img):
		self.real = real
		self.img = img
	def __add__(self,otherObject):
		return self.real+otherObject.real,self.img+otherObject.img
	def __sub__(self,otherObject):
		return self.real-otherObject.real,self.img-otherObject.img
	def __mul__(self,otherObject):
		rreal = self.real*otherObject.real-(self.img*otherObject.img)
		rimg = self.real*otherObject.img + otherObject.real*self.img
		return rreal,rimg
obj1 = complex(3,4)
obj2 = complex(2,1)
obj3 = obj1+obj2
obj4 = obj1+obj2
print(obj4)