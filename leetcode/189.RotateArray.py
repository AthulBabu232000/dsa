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
