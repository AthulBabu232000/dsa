arr=[-1,0,1,2,-1,-4]
def threeSum(arr):
    start=0
    end=len(arr)-1
    finalResult=list()
    temp=0
    arr.sort()
    while(start<end):
        print(temp)
        print(start,end)
        temp=arr[start]+arr[end]
        if(-1*temp in arr):
            finalResult.append([arr[start],arr[end],-1*temp])
        elif(temp>0):
            end=end-1
        elif(temp<0):
            start=start+1
    return finalResult
result=threeSum(arr)
print(result)