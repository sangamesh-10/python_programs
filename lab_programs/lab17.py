class Node:
    data = None
    next = None
    previous = None
    def __init__(self,val) -> None:
        self.data = val
        self.next = None
        self.previous = None
class deque:
    front = None
    rear=None
    size = 0
    def Enqueue(self,elem):
        t= Node(elem)
        if self.front == None:
            self.front = self.rear = t
            self.size+=1
        else:
            t.previous = self.rear
            self.rear.next = t
            self.rear = t
            self.size+=1
    def Enqueue_front(self,elem):
        t = Node(elem)
        if self.front == None:
            self.front = self.rear = t
            self.size+=1
        else:
            t.next = self.front
            self.front.previous = t
            self.front = t
            self.size+=1
    def Dequeue(self):
        if self.front == None:
            print("the Queue is empty...")
            return
        elif self.front == self.rear:
            delv = self.front.data
            self.front = self.rear = None
            self.size-=1
            print("the Queue is now empty...")
            return delv
        else:
            delv = self.front.data
            self.front = self.front.next
            self.front.previous = None
            self.size-=1
            return delv
    def Dequeue_rear(self):
        if self.front == None:
            print("Queue is empty...")
            return
        elif self.front == self.rear:
            delv = self.front.data
            self.front = self.rear = None
            self.size-=1
            print("the Queue is now empty...")
            return delv
        else:
            itr = self.front
            while itr.next!= self.rear:
                itr = itr.next
            itr.next = None
            delv = self.rear.data
            self.rear = itr
            self.size-=1
    def display(self):
        itr = self.front
        if itr == None:
            print("the Queue is empty...")
            return
        print("Front",end = "'-> {")
        while itr!=None:
            print(itr.data,end=",")
            itr = itr.next
        print("}<-'Rear")
    def display_Rev(self):
        itr = self.rear
        if itr== None:
            print("the Queue is w=empty...")
            return
        else:
            while itr!=None:
                print(itr.data,end = " ")
                itr = itr.previous
t = deque()
t.Enqueue(1)    
t.Enqueue(3)    
t.Enqueue(4)    
t.Enqueue(6)
t.Dequeue()
t.Enqueue_front(2)
t.Enqueue_front(1)
t.Dequeue_rear()
t.Enqueue(5)
t.Enqueue(6)
t.display_Rev()    