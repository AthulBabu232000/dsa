nums = [2, 4, 6, 8, 10, 12]
target = 8
def targetFinder(nums, target):
    start=0
    end=len(nums)-1
    while(end>=start):
        if(nums[start]+nums[end]==target):
            return[start,end]
        elif(nums[start]+nums[end]>target):
            end=end-1
        elif(nums[start]+nums[end]<target):
            start=start+1
print(targetFinder(nums,target))