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
# iterating through linkedlist headA 
current=headA 
nodevaluesA=list()
while(current is not None):
    print(current.val,end=" ")
    nodevaluesA.append(current)
    current=current.next 
# iterating through linkedlist headB 
print()
current=headB 
nodevaluesB=list()
while(current is not None):
    print(current.val,end=" ")
    nodevaluesB.append(current)
    current=current.next 
print()
# iterates through either of linkedlist to find the intersection node: 
for i in nodevaluesB:
    if i in nodevaluesA:
        print("the value is found")
        print(i.val)
# the above code worked but there is time exceeding issue existing 
# let me think with hashmap intuition for the problem now


