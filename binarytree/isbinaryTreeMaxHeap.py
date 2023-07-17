# Given a binary tree. The task is to check whether the given tree follows the max heap property or not.

class Node:
    def __init__(self,value):
        self.value=value 
        self.left=None 
        self.right=None 
root=Node(5)
b=Node(3)
c=Node(2)
root.left=b 
root.right=c 
queue=[root]
depth=0
values=list()
while(len(queue)>0):
    levelsize=len(queue)
    depth+=1
    for i in range(levelsize):
        current=queue.pop(0)
        if current is not None: values.append(current.value)
        else: values.append("N")
        if current is not None:
            if current.left is not None:queue.append(current.left)
            else: queue.append(None)
            if current.right is not None:queue.append(current.right)
            else: queue.append(None)
print(values,depth)
flag=0
for i in range(depth-3):
    if values[2*i+1]!="N" or values[2*i+2]:
        flag=1
        break
    elif values[i]>values[2*i+1] and values[i]>values[2*i+2]:
        continue 
    else:
        flag=1
        break
if flag==0:
    print("it is a maxheap")
else:
    print("it is not a max heap")
