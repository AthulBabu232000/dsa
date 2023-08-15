class Node:
    def __init__(self,value):
        self.value=value 
        self.next=None 
head=Node(1)
first=Node(2)
second=Node(3)
fourth=Node(4)
fifth=Node(5)

# write a function which remove nth element from the end of the linkedlist 
head.next=first
first.next=second 
second.next=fourth 
fourth.next=fifth 
fifth.next=None 

def remove(head:Node,node_count:int):
    current=head 
    node_finder=1 # removing the first element is not working
    while(current is not None):
        node_finder+=1 
        if node_finder==node_count and current.next is not None:
            current.next=current.next.next
        current=current.next 

def printLinkedList(head:Node):
    current=head 
    nodevalues=list()
    while(current is not None):
        nodevalues.append(current.value)
        current=current.next
    return nodevalues 

output:list[int]=printLinkedList(head)
print(output)
remove(head,1)
alternate_output:list[int]=printLinkedList(head)
print(alternate_output)
# this is the code i did in leetcode 
# iterate through linkedlist
# take those values in a list
# remove the element required 
# add the updated values list into a linkedlist 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    values=list()
    current=head 
    while(current is not None):
        values.append(current.val)
        current=current.next 
    print(values)
    remove_el_index=len(values)-n 
    values.pop(remove_el_index)
    print(values)
    if len(values)==0:return None
    newNode=ListNode(0)
    current=newNode 
    for i in range(len(values)):
        current.next=ListNode(values[i])
        current=current.next 
    return newNode.next