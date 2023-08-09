# binary tree inorder traversal 
# traversal left subtree 
# visit node 
# traversal right subtree 
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right 
        self.left=left 

node=Node(1)
two=Node(2)
three=Node(3)
node.right=two 
two.left=three 
values=list()
def inorderTraversal(node,values):
    if not node:return 
    inorderTraversal(node.left,values)
    values.append(node.value)
    inorderTraversal(node.right,values)
    return values
output=inorderTraversal(node,values)
print(output)
