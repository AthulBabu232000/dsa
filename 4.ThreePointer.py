arr = [-4, -2, -1, 0, 1, 2, 3]
target=0
n=len(arr)
triplets=list()
def findTriplets(arr):
    for i in range(n-2):
        left=i+1
        right=n-1
        while(left<right):
            temp=arr[i]+arr[left]+arr[right]
            if(temp==target):
                triplets.append([arr[i],arr[left],arr[right]])
                left=left+1
                right=right-1
            elif(temp<target):
                left=left+1
            else:
                right=right-1
    return triplets
result=findTriplets(arr)
print(result)

