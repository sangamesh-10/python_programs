class Node:
    data = None
    next = None
    def __init__(self,val) -> None:
        self.data = val
        self.next = None
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.length = 0
    def Enqueue(self,elem):
        t= Node(elem)
        if self.front == None:
            self.front = self.rear = t
            self.length+=1
        else:
            self.rear.next = t
            self.rear = t
            self.length+=1
    def Dequeue(self):
        if self.front == None:
            print("the Queue is empty...")
            return
        elif self.front == self.rear:
            delv = self.front.data
            self.front = self.rear = None
            self.length-=1
            print("the Queue is now empty...")
            return delv
        else:
            delv = self.front.data
            self.front = self.front.next
            self.length-=1
            return delv
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False
    def len(self):
        return self.length
    def printQueue(self):
        if self.length == 0:
            print("the Queue is empty...")
        else:
            itr = self.front
            while itr!=None:
                print(itr.data,end = " ")
                itr = itr.next
            print()
q= Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
q.Enqueue(6)
q.Enqueue(7)

q.printQueue()
q.Dequeue()
q.isEmpty()
q.Dequeue()
q.printQueue()
print(q.len())