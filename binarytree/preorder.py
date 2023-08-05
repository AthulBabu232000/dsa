# its almost same as dfs 
# visit the current node 
# traverse the left node 
# traverse the right node 
import classNode as cn 

def preOrder(node,valuesList):
    if not node:return
    valuesList.append(node.value)
    preOrder(node.left,valuesList)
    preOrder(node.right,valuesList)
    return valuesList 

values=list()
result=preOrder(cn.one,values)
print(result)