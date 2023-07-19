mainString="hellothisisthebeginningofthenewworld"
subString="orld"
def findString(main,sub,real):
    sizeMain=len(main)
    sizeSub=len(sub)
    if sizeSub==0: return True 
    if sizeMain==0:return False 
    if main[0]==sub[0]:
        return findString(main[1:],sub[1:],real)
    else:
        sub=real
    return findString(main[1:],sub,real)  
result=findString(mainString,subString,subString)
print(result)
if subString in mainString:
    print("yes it is present")
else:
    print("no not present")