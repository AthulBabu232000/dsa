arr="1 box has 3 blue 4 red 6 green and 12 yellow marbles"
def asc(arr):
    iterables=arr.split(' ')
    numList=list(map(int,filter(lambda x:x.isdigit(),iterables)))
    print(numList)
    for i in range(len(numList)-1):
        if numList[i+1]<=numList[i]:
            return False 
    return True
result=asc(arr)
print(result)