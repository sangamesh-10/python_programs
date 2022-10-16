class Queue:
    def __init__(self) -> None:
        self.front = -1
        self.rear = -1
        self.queue = []
        print("Queue is initialized with no elements...")
    def enqueue(self,elem):
        if self.front == -1:
            self.front = self.rear = 0
            self.queue.append(elem)
        else:
            self.rear+=1
            self.queue.append(elem)
    def dequeue(self):
        if self.front == -1:
            print("The Queue is empty...")
            return
        if self.front == self.rear:
            self.front = self.rear = -1
            self.queue.pop()
        else:
            self.rear-=1
            self.queue.pop(0)
    def isEmpty(self):
        if self.front == -1:
            return True
        else:
            return False
    def printQueue(self):
        print(self.queue)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print(q.front)
print(q.rear)
q.printQueue()