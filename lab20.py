class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1
    def push(self,elem):
            self.top+=1
            self.stack.append(elem)
    def pop(self):
        if self.top ==-1:
            print("Stack is Empty...")
            return
        else:
            self.top-=1
            delv = self.stack[self.top]
            self.stack.pop()
            return delv
    def peek(self):
        if self.top == -1:
            print("Stack has no elements...")
            return
        else:
            print(self.stack[self.top])
            return
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def len(self):
        return len(self.stack)
    def print(self):
        print(self.stack)
st = Stack()
print(st.isEmpty())
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.print()
st.pop()
st.peek()

        