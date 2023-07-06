class Node:
    def __init__(self,value=0) -> None:
        self.value=value 
        self.next=None 

class sLinkedList:
    def __init__(self) -> None:
        self.headvalue=None 

head=sLinkedList()
head.headvalue=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
head.headvalue.next=b
b.next=c 
c.next=d 
d.next=None 

def printList():
    current=head.headvalue 
    while(current is not None):
        print(current.value)
        current=current.next 

def atBeginning(value):
    tempnode=Node(value)
    tempnode.next=head.headvalue
    head.headvalue=tempnode 

printList()
atBeginning("z")
print("\nAfter adding new node:")   
printList()

# remove node b from the linkedlist 
def removeNode(nodeB):
    current=head.headvalue
    while(current is not None):
        if current.next == nodeB and current.next is not None:
            current.next=nodeB.next 
        current=current.next 

printList()
print("printing after removing node b ")
removeNode(d)
printList()
