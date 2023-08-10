def isSameTree(self, p, q):
    if q is None and p is not None:
        return False 
    elif p is None and q is not None:
        return False 
    elif p is None and q is None:
        return True
    queueP=[p]
    queueQ=[q]
    values=list()
    while(len(queueP)>0 and len(queueQ)>0):
        currentP=queueP.pop(0)
        currentQ=queueQ.pop(0)
        if currentP.val!=currentQ.val:
            return False
        if currentP.left is not None and currentQ.left is not None:
            queueP.append(currentP.left)
            queueQ.append(currentQ.left)
        elif currentP.left is None and currentQ.left is not None:
            return False 
        elif currentP.left is not None and currentQ.left is None:
            return False
        if currentP.right is not None and currentQ.right is not None:
            queueP.append(currentP.right)
            queueQ.append(currentQ.right)
        elif currentP.right is None and currentQ.right is not None:
            return False 
        elif currentP.right is not None and currentQ.right is None:
            return False
    if(len(queueP)>0 or len(queueQ)>0):
        return False 
    return True
