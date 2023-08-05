# traverse the left side 
# traverse the right side 
# visit the current node 

import classNode as cn


def postOrder(node,valuesList):
    if not node:return 
    postOrder(node.left,valuesList)
    postOrder(node.right,valuesList)
    valuesList.append(node.value)
    return valuesList 

values=list()
result=postOrder(cn.one,values)
print(result)
