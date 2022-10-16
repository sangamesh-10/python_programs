class Node:
    # data = None
    # next = None
    # previous = None
    def __init__(self,val) -> None:
        self.data = val
        self.previous = None
        self.next = None
class double_ll:
    head = None
    tail = None
    def insert(self,elem):
        t=Node(elem)
        if(self.head==None):
            self.head = self.tail = t
        else:
            self.tail.next = t
            self.tail = t
    def delete(self,elem):
        if self.head == None:
            print("the list is empty ..cannot delete...")
            return
        if self.head.data == elem:
            if self.head == self.tail:
                self.head = self.tail = None
                return
            else:
                # self.head.next.previous = None
                self.head = self.head.next
                self.head.previous = None
                return
        itr = self.head
        while itr!=self.tail and itr.next.data!=elem:
            itr = itr.next
        if itr == self.tail:
            print("element not present in list....")
            return
        if itr.next == self.tail:
            itr.next = None
            self.tail = itr
            return
        itr.next = itr.next.next
        itr.next.previous = itr
        return
    def display(self):
        if self.head == None:
            print("list has no elements....")
            return
        itr = self.head
        while itr!=None:
            print(itr.data,end = "->")
            itr= itr.next
dl = double_ll()
dl.insert(1)   
dl.insert(2)   
dl.insert(3)   
dl.insert(4)   
dl.insert(5)
dl.delete(6)
dl.display()