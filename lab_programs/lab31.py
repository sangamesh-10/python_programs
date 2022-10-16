class Bst:
	class Node:
		def __init__(self,data):
			self.data = data
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
	def preorder(self,root):
		if root == None:
			return
		print(root.data,end = " ")
		self.preorder(root.left)
		self.preorder(root.right)
	def postorder(self,root):
		if root == None:
			return
		self.postorder(root.left)
		self.postorder(root.right)
		print(root.data,end = " ")
val = [5,6,9,3,1,8,0,2,7,4]
bt = Bst()
root = None
for i in val:
	root = bt.insert(root,i)
bt.inorder(root) 
print()
bt.preorder(root)
print()
bt.postorder(root)