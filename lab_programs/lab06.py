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
		rreal = round(self.real*otherObject.real-(self.img*otherObject.img),2)
		rimg = round(self.real*otherObject.img + otherObject.real*self.img,2)
		return rreal,rimg
obj1 = complex(3.5,4.1)
obj2 = complex(2.1,1.5)
obj3 = obj1*obj2
print(obj3)