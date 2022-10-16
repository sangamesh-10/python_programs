def inp_prec(ns):
	find1 = {'+':1,'-':1,'*':3,'/':3,'^':6,'(':9,')':0}
	if ns in find1.keys():
		return find1[ns]
	else:
		return 7
def stk_prec(ns):
	find1 = {'+':2,'-':2,'*':4,'/':4,'^':5,'(':0,')':0}
	if ns in find1.keys():
		return find1[ns]
	else:
		return 8
class stack:
	top=-1
	values = []
	def isEmpty(self):
		if(len(self.values)==0):
			return True
		else:
			False
	def push(self,elem):
		self.values.append(elem)
		self.top+=1;
	def pop(self):
		if self.isEmpty():
			print("stack is full")
		else:
			data = self.values[self.top]
			self.values.pop()
			self.top-=1
			return data
	
infix = input("enter the infix expression :")+")#"
postfix =""
s= stack();
s.push('(')
for i in infix:
	if i=='#':
		break;
	while inp_prec(i)<stk_prec(s.values[s.top]):
		postfix=postfix + s.pop()
	if inp_prec(i)>stk_prec(s.values[s.top]):
		s.push(i)
	else:
		s.pop()
print(postfix)