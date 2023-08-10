class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val 
        self.right=right 
        self.left=left 

node=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)

node.left=two 
node.right=three 
two.left=four 
two.right=five 
three.left=six 


stack=[node]
values=list()
while(len(stack)>0):
    current=stack.pop()
    print(current.val)
    values.append(current.val)
    if current.right is not None: stack.append(current.right)
    if current.left is not None: stack.append(current.left)
print(values)