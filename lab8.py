def isOperater(ch):
	operator=['+','-','*','^','/']
	if ch in operator:
		return True;
	else:
		return False
def calculate(a,b,opr):
	if opr == "+":
		return a+b
	elif opr == '-':
		return b-a
	elif opr == '*':
		return a*b
	elif opr == '^':
		return b**a
	elif opr == '/':
	    return b/a
	else:
		print("invalid operator")
		return

postfix = input("Enter the postfix expression : ")
list=[]
for i in postfix:
	if isOperater(i):
		val1=int(list.pop())
		val2 = int(list.pop())
		result = calculate(val1,val2,i)
		list.append(result)
	else:
		list.append(i)
print(list[0])
