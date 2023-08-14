class Node:
    def __init__(self,value):
        self.value=value 
        self.next=None 
head=Node(1)
first=Node(2)
# write a function which remove nth element from the end of the linkedlist 
def printNodeVal(head):
    values=list() 
    current=head 
    while(current is not None):
        values.append(current.value)
        current=current.next 
    return values 

def nodeLength(head):
    length=1 
    current=head 
    while(current is not None):
        length+=1
        current=current.next 
    return length
length=nodeLength(head)
print(length)
n:int=input("enter the node number from end to remove: ")
remove_el_index=length-n
def removeNode(head,remove_el_index):
    length=1
    current=head
    while(current is not None):
        length+=1
        if length==remove_el_index: 
            current.next=current.next.next
        current=current.next 
result_expected=removeNode(head,remove_el_index)
output_expected=printNodeVal(head)
print(output_expected)


