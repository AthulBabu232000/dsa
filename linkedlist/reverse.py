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

# reversing the list 
for i in range(n//2):
    temp=revList[i]
    revList[i]=revList[n-i-1]
    revList[n-i-1]=temp

# setting reversed value in array to linkedlist nodes 
head.headvalue=revList[0]
current=head.headvalue
for i in revList[1:]:
    current.nextvalue=i
    current=current.nextvalue 
current.nextvalue=None
print("reversing the linkedlist")
printList()






# the classic way of reversing the linkedlist 

header=Node('1')
body1=Node('2')
body2=Node('3')
body3=Node('4')
footer=Node('5')
header.nextvalue=body1 
body1.nextvalue=body2 
body2.nextvalue=body3 
body3.nextvalue=footer 
footer.nextvalue=None 

current=header 
while(current is not None):
    print(current.datavalue)
    current=current.nextvalue 

print("reversing the linkedlist in classic way by reversing the pointer while traversing")
# here i use two pointers one is "prev" which is null initially and "current" points to
# first element in the beginning 
prev=None 
current=header 
while(current is not None):
    temp=current
    current=current.nextvalue
    temp.nextvalue=prev 
    prev=temp
# when the traversal ends prev points to the last element
# actually their linkage is reversed 
# finally printing to conform the reversal 
current=prev 
while(current is not None):
    print(current.datavalue)
    current=current.nextvalue 





