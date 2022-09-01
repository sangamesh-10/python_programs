class Node:
    data = None
    next = None
    def __init__(self,val) -> None:
        self.data = val
        self.next = None        
class Stack:
    def __init__(self) -> None:
       self.top =None
       self.length = 0
       print("Stack is created with no elements...")
    def push(self,elem):
       t= Node(elem)
       if self.top == None:
           self.top = t
           self.length+=1
       else:
           t.next = self.top
           self.top = t
           self.length+=1
    def pop(self):
        if self.top == None:
            print("Stack is empty...")
            return
        delv = self.top.data
        self.top = self.top.next
        self.length-=1
        return delv
    def display(self):
        itr = self.top
        if itr == None:
            print("the list is empty...")
            return
        else:
            while itr!=None:
                print(itr.data)
                itr = itr.next
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    def peek(self):
        if self.top == None:
            print("Stack has No elements...")
            return
        else:
           print(self.top.data)
           return
st = Stack()
st.push(1)
# st.push(2)
# st.push(3)
# st.push(4)
# st.push(5)
# st.display()
st.pop()
st.peek()
print(st.length)
