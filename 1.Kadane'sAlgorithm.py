arr = [-2, -3, 4, -1, -2, 1, 5, -3]
#find the maximum sum from the subarray=>continous memory
def kadane(arr):
    maxi=min(arr)
    current=0
    for i in range(len(arr)):
        current+=arr[i]
        if current>maxi:
            maxi=current
        if current<0:
            current=0
    return maxi
print(kadane(arr))
