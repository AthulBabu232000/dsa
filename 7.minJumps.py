def minJumps(arr,n):
    pointer=0 
    count=0 
    while(pointer<n):
        if arr[pointer]==0:
            return -1
        else:
            pointer+=arr[pointer]
            count+=1 
        print(pointer)
    return count 
arr=[1,3,5,8,9,2,6,7,6,8,9]
arr1=[2,3,1,1,2,4,2,0,1,1]
n=11
result=minJumps(arr1,n)
print(result)
# this code is not right
        
