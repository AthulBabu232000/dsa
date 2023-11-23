class Node:
    def __init__(self,val,next=None) -> None:
        self.val=val 
        self.next=None 

head=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
head.next=two 
two.next=three 
three.next=four 
def printNode(head:Node)->list[int]:
    current=head
    values=list() 
    while(current is not None):
        values.append(current.val)
        current=current.next 
    return values 

def swapNode(head:Node)->Node:
    counter=1 
    current=head 
    while(current is not None):
        print(current.val)
        if counter%2!=0:
            if current.next is not None:
                temp=current
                current=current.next 
                current.next=temp 
                current=temp
            else:
                current=current.next 
        else:
            current=current.next 
        counter+=1 
    return head 
inputnode=printNode(head)
output=swapNode(head)
# result=printNode(output)
print(inputnode)
