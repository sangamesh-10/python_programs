class Node:
	data = None
	next = None
	def __init__(self,val):
		self.data = val
		self.next = None
class Linkedlist:
	Head = None
	Tail = None
	def insert(self,elem):
		t = Node(elem)
		if self.Head == None:
			self.Head = t
			self.Tail = t
		else:
			self.Tail.next = t
			self.Tail = t
	def delete(self,elem):
		if self.Head == None:
			print("the list is empty")
			return
		if self.Head.data == elem:
			if self.Head == self.Tail:
				self.Head = self.Tail = None
				return
			else:
				self.Head = self.Head.next
				return
		itr = self.Head
		while itr.next.data != elem and itr!=None:
			itr = itr.next
		if itr== None:
			print("element not present.....")
		itr.next = itr.next.next
	def display(self):
		itr = self.Head
		while itr!=None:
			print(itr.data,end = "->")
			itr = itr.next		
p = Linkedlist()
p.insert(1)
p.insert(2)
p.insert(3)
p.insert(4)
p.insert(5)
p.delete(1)
p.display()