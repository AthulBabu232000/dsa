givenList=[1,23,4,2,5]
def addList(givenList):
    if len(givenList)==1:
        return givenList[0]
    return givenList[0]+addList(givenList[1:])

print("result of sum of all elements in a list using recursion: in python")
result=addList(givenList)
print(result)