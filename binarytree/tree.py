class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None

#               a
#              / \
#             b   c
#            / \   \
#           d  e    f
# binary tree we are using to create => Binary Search Tree(BST)

rootNode=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')

rootNode.left=b 
rootNode.right=c 
b.left=d 
b.right=e 
c.right=f 


# applying the depth first algorithm
# create a value array 
# to print all the values of the nodes in the tree
# dfs=>use stack

def dfs_traversal(root):
    stack=[root]
    values=list()
    if root==None:
        values=[]
        return values 
    while(len(stack)>0):
        current=stack.pop()
        values.append(current.value)
        if current.right is not None: stack.append(current.right)
        if current.left is not None: stack.append(current.left)
    return values

print(dfs_traversal(rootNode))
    
        
# applying the breadth first algorithm
# create a value array 
# to print all the values of the nodes in the tree
# dfs=>use queue

def bfs_traversal(root):
    values=list()
    queue=[root]
    if root is None: 
        values=[]
        return values
    while(len(queue)>0):
        current=queue.pop(0)
        values.append(current.value)
        if current.left is not None: queue.append(current.left)
        if current.right is not None: queue.append(current.right)
    return values

print(bfs_traversal(rootNode))