# in this problem we are given two nodes say p,q and 
# we have to analyse if the values of p and q tree are identical
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
# this is js version using recursion
# class Solution {
#     public boolean isSameTree(TreeNode p, TreeNode q) {
#         if(p==null && q==null)
#         return true;
#         if(p!=null&&q!=null)
#         {
#             return ( (p.val==q.val)&&(isSameTree(p.left,q.left))&& (isSameTree(p.right,q.right)));
#         }
#         return false;
#       }
      
#     }