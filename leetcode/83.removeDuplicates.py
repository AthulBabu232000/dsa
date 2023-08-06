class Node:
    def __init__(self,value=0) -> None:
        self.value=value 
        self.next=None 

a=Node(1)
b=Node(1)
c=Node(1)
d=Node(4)
e=Node(4)
a.next = b
b.next = c
c.next = d 
d.next = e 
e.next = None
# while writing the function consider the case if head is not None: anyway return head 
current=a 
while(current is not None):
    el=current
    while(el is not None):
        if el.value==current.value:
            el=el.next 
        else: break 
    current.next=el
    current=current.next
current=a 
while(current is not None):
    print(current.value)
    current=current.next 



