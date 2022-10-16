class Bst1:
	class Node:
		def __init__(self,val) -> None:
			self.data = val
			self.left = None
			self.right = None
	def insert(self,root,val):
		if root == None:
			root = self.Node(val)
			return root;
		cur = root
		prev = None
		while(cur):
			prev = cur
			if cur.data > val:
				cur = cur.left
			elif cur.data < val:
				cur = cur.right
			else:
				return root
		if val < prev.data:
			prev.left = self.Node(val)
		else:
			prev.right = self.Node(val)
		return root
	def inorder(self,root):
		if root == None:
			return
		self.inorder(root.left)
		print(root.data,end = " ")
		self.inorder(root.right)
	def nrSearch(self,root,key):
		if(root is None):
			print("tree is empty..")
			return
		while root != None:
			if root.data == key:
				print("search sucessful...")
				return
			elif root.data <key:
				root = root.right
			else:
				root = root.left
		print("element not found..")
	def rSearch(self,root,key):
		if root is None:
			print("element not found..")
			return
		if(root.data == key):
			print("search succesfull...")
			return
		elif key < root.data:
			self.rSearch(root.left,key)
		else:
			self.rSearch(root.right,key)
		
val = [5,6,9,3,1,8,0,2,7,4]
bt = Bst1()
root = None
for i in val:
	root = bt.insert(root,i)
bt.inorder(root)
key = int(input("enter the integer to search-->"))
bt.rSearch(root,key)