class Node:
    def __init__(self,datavalue):
        self.datavalue=datavalue 
        self.nextvalue=None 

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
# here i use two pointers one is "prev" which is null initially and "current" points to first element in the beginning 
prev=None 
current=header 
while(current is not None):
    temp=current
    current=current.nextvalue
    temp.nextvalue=prev 
    prev=temp
# when the traversal ends prev points to the last element
current=prev 
while(current is not None):
    print(current.datavalue)
    current=current.nextvalue 

