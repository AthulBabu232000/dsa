# you are given an array 
# you are given a target
# return the index of start and final position of subarray
# sum(subarray)=target
def subArray(arr,target,n):
    start=0
    end=1 
    result=[]
    current=arr[0]
    while(end<=n):
        if(current==target):
            result.append(start+1)
            result.append(end)
            return result 
        while(current>target and start<end-1):
            current-=arr[start]
            start+=1 
        if end<n:
            current+=arr[end]
        end+=1
    result.append(-1)
    return result
arr=[1,2,3,4,5,6,7,8,9,10]
final=subArray(arr,15,10)
print(final)
