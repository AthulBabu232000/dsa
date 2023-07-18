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
def addToList():
    revList=list() 
    current=head.headvalue
    while(current is not None):
        revList.append(current)
        current=current.nextvalue
    return revList
revList=addToList()
n=len(revList)
for i in range(n//2):
    temp=revList[i]
    revList[i]=revList[n-i-1]
    revList[n-i-1]=temp
head.headvalue=revList[0]
current=head.headvalue
for i in revList[1:]:
    current.nextvalue=i
    current=current.nextvalue 
current.nextvalue=None
print("reversing the linkedlist")
printList()

