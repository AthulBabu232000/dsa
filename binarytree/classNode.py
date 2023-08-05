class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value 
        self.left=left 
        self.right=right 
one=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6) 
seven=Node(7)

one.left=two 
one.right=three 
two.left=four 
two.right=five 
three.left=six 
three.right=seven 