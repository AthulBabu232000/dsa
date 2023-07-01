class Node:
    def __init__(self,datavalue=0) -> None:
        self.datavalue=datavalue
        self.nextvalue=None

class sLinkedList:
    def __init__(self) -> None:
        self.headvalue=None

head=sLinkedList()
head.headvalue=Node(1)
body1=Node(2)
body2=Node(4)
head.headvalue.nextvalue=body1
body1.nextvalue=body2
body2.nextvalue=None

head2=sLinkedList()
head2.headvalue=Node(1)
body3=Node(3)
body4=Node(4)
head2.headvalue.nextvalue=body3
body3.nextvalue=body4
body4.nextvalue=None
current=head.headvalue
print("printing the value of linkedlist")
while(current is not None):
    print(current.datavalue)
    current=current.nextvalue
print("finished printing")
current=head2.headvalue
while(current is not None):
    print(current.datavalue)
    current=current.nextvalue
result=Node()
dummy=result
while(head.headvalue is not None and head2.headvalue is not None):
    if(head.headvalue.datavalue<head2.headvalue.datavalue):
        result.nextvalue=head.headvalue
        head.headvalue=head.headvalue.nextvalue
    elif(head.headvalue.datavalue>head2.headvalue.datavalue):
        result.nextvalue=head2.headvalue
        head2.headvalue=head2.headvalue.nextvalue
    else:
        result.nextvalue=head.headvalue
        head.headvalue=head.headvalue.nextvalue
        result=result.nextvalue
        result.nextvalue=head2.headvalue
        head2.headvalue=head2.headvalue.nextvalue
    result=result.nextvalue
print("printing value of result")
current=dummy.nextvalue
while(current is not None):
    print(current.datavalue)
    current=current.nextvalue


