mainString="hellothisisthebeginningofthenewworld"
subString="ord"
def findString(main,sub):
    sizeMain=len(main)
    sizeSub=len(sub)
    if sizeSub==0: return True 
    if sizeMain==0:return False 
    if main[0]==sub[0]:
        return findString(main,sub)
    return findString(main[1:],sub)
result=findString(mainString,subString)
print(result)