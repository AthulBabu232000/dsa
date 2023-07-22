arr=[1,2,3,4,5,6,7,8]
# output is [6,7,8,1,2,3,4,5]
k=3 
# task is to rotate array without using extra space 
# already got an answer using insertion sort algorithm O(n2)
def rotateArray(nums,k):
    if len(nums)==2 and k%2!=0:
        nums.reverse()
    else:
        temp=nums[len(nums)-k:]
        temp.extend(nums[:len(nums)-k])
        for i in range(len(temp)):
            nums[i]=temp[i]
    return nums

arr=[1,2]
k=5 
result=rotateArray(arr,k)
print(result)

# here is another code with much better space complexity for rotating an array 
# by k 
def rotate(self, nums, k):
    nums.reverse()
    n=len(nums)-1 
    k=k%(n+1)
    i=0 
    j=k-1
    while(i<j):
        nums[i],nums[j]=nums[j],nums[i]
        i+=1 
        j-=1 
    i=k
    j=n 
    while(i<j):
        nums[i],nums[j]=nums[j],nums[i]
        i+=1 
        j-=1 
    return nums
