class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedLists:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def detectLoop(self):
        if self.head==None:
            return None
        fast=self.head
        slow=self.head

        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                self.removeLoop(slow)
                return 1
        return 0
    def removeLoop(self,nodel):
        ptr1=nodel
        ptr2=nodel

        k=1
        while(ptr1.next!=ptr2):
            ptr1=ptr1.next
            k=k+1

        ptr1=self.head
        ptr2=self.head

        for i in range(k):
            ptr2=ptr2.next

        while(ptr2!=ptr1):
            ptr1=ptr1.next
            ptr2=ptr2.next

        while(ptr2.next!=ptr1):
            ptr2=ptr2.next
        ptr2.next=None
    def printList(self):
        current=self.head
        while(current!=None):
            print(current.data,end='->')
            current=current.next
        print('Null')
if __name__=='__main__':
    l=LinkedLists()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(5)
    
    l.head.next.next.next.next.next = l.head.next.next
    l.detectLoop()
    l.printList()