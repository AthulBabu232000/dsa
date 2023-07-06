class Node:
    def __init__(self,datavalue=0) -> None:
        self.datavalue=datavalue 
        self.nextvalue=None

class sLinkedList:
    def __init__(self) -> None:
        self.headvalue=None

head=sLinkedList()
head.headvalue=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
z=Node('z')
head.headvalue.nextvalue=b 
b.nextvalue=c 
c.nextvalue=d 
d.nextvalue=z 
z.nextvalue=None 

def printList():
    current=head.headvalue
    while current is not None: 
        print(current.datavalue)
        current=current.nextvalue
printList()
