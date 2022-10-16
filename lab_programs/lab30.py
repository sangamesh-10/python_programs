class Deque:
    def __init__(self) -> None:
        self.list = []
        self.front = -1
        self.rear = -1
    def Enqueue(self,elem):
        if self.front == -1:
            self.list.append(elem)
            self.front+=1
            self.rear +=1
        else:
            self.list.append(elem)
            self.rear+=1
    def Enqueue_front(self,elem):
        if self.front == -1:
            self.list.append(elem)
            self.front+=1
            self.rear +=1
        else:
            self.list.insert(0,elem)
            self.rear+=1
    def Dequeue(self):
        if self.front == -1:
            print("the list is empty..")
        else:
            
            if(self.front == self.rear):
                self.list.pop(0)
                self.front = self.rear = -1
                return
            self.list.pop(0)
            self.rear-=1
    def Dequeue_rear(self):
        if self.front == -1:
            print("the list is empty..cannot delete")
            return
        else:
            if(self.front == self.rear):
                self.list.pop()
                self.front = self.rear = -1
                return        
            self.list.pop()
            self.rear-=1
    def isEmpty(self):
        if len(self.list == 0):
            return True
        else:
            return False
    def display(self):
        print(self.list)
    def Front(self):
        print(self.list[self.front])
    def Rear(self):
        print(self.list[self.rear])
dq=Deque()
dq.Enqueue(1)
dq.Enqueue(2)
dq.Enqueue(3)
dq.Enqueue(4)
dq.Enqueue_front(0)
dq.display()
dq.Dequeue()
dq.Dequeue_rear()
dq.Front()
dq.Rear()
dq.display()