class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Binary Tree Structure
#               1
#              / \
#             2   2
#            / \ 
#           3   3
#          / \
#         4   4

root = Node(1)
b = Node(2)
c = Node(2)
d = Node(3)
e = Node(3)
f = Node(4)
g = Node(4)
root.left = b
root.right = c
b.left = d
b.right = e
d.left = f
d.right = g
# the above mentioned tree is not a balanced binary tree as left and right of a node has depth difference greater than 1
# let me create another tree where my testcase failed earlier here it comes dude 


# root=Node(1)
# b=Node(2)
# c=Node(3)
# root.right=b 
# b.right=c 
# this is my second test case 




# root=Node(1)
# b=Node(2)
# c=Node(2)
# d=Node(3)
# e=Node(3)
# f=Node(4)
# g=Node(4)
# root.left=b 
# root.right=c 
# b.left=d 
# c.right=e 
# d.left=f 
# e.right=g 
# this is my third testcase where i failed before


#findDepth function finds the depth of each node it used bfs algorithm and queue idea 
#bfs_traversal iterates over all nodes present along with the findDepth find the depth of all nodes
#diff variable holds the difference in depth of current left and right nodes 
#if diff is greater than 1 then it is not a balanced tree 

def findDepth(node):
    nodeQueue=[node]
    nodeDepth=0 
    while(len(nodeQueue)>=1):
        levelsize=len(nodeQueue)
        nodeDepth+=1
        for i in range(levelsize):
            currentQueue=nodeQueue.pop(0)
            if currentQueue.left is not None: nodeQueue.append(currentQueue.left)
            if currentQueue.right is not None: nodeQueue.append(currentQueue.right)
    return nodeDepth
 


def bfs_iterator(root):
    depth=0
    depthl,depthr=0,0
    queue=[root]
    while(len(queue)>0):
        levelsize=len(queue)
        depth+=1 
        for i in range(levelsize):
            current=queue.pop(0)
            if current.left is not None:
                queue.append(current.left)
                depthl=findDepth(current.left)
            if current.right is not None:
                queue.append(current.right)
                depthr=findDepth(current.right)
            if current.right is None:
                depthr=0 
            if current.left is None: 
                depthl=0 
            diff=abs(depthl-depthr)
            if diff>1:
                return False 
    return True 

result=bfs_iterator(root)
print(result)