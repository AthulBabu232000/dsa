class Node: 
    def __init__(self,val,next=None):
        self.val=val 
        self.next=next 
# creating two linkedlist 
# headA [4,1,8,4,5]
# headB [5,6,1,8,4,5]
headA=Node(4)
one=Node(1)
two=Node(8)
three=Node(4)
four=Node(5)
headB=Node(5)
five=Node(6)
six=Node(1)
headA.next=one 
one.next=two
two.next=three 
three.next=four 
headB.next=five
five.next=six 
six.next=two 


def intersect(headA,headB):
    lenA=0 
    lenB=0 
    current=headA 
    while(current is not None):
        lenA+=1 
        current=current.next 
    current=headB 
    while(current is not None):
        lenB+=1 
        current=current.next 
    length=min(lenA,lenB)

