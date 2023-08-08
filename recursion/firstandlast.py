s="abaacdaefaah"


def occurence(s,c,i,indexs):
    if len(s)==0:
        return
    if(s[0]==c):
        indexs.append(i)
    occurence(s[1:],c,i+1,indexs)
    if len(indexs)>0:
        return [indexs[0],indexs[len(indexs)-1]]
    return 


c:str=input("enter the character: ")
i:int=0
indexs:int=list()
result=occurence(s,c,i,indexs)
print(result)