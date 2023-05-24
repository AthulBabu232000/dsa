arr = [-2, 10, -4, -1, -2, -1, -5, -3]
k=5
def slidingWindow(arr,k):
    arraySum=sum(arr[:k])
    maximum=arraySum
    n=len(arr)
    for i in range(n-k):
        arraySum=arraySum-arr[i]+arr[i+k]
        maximum=max(arraySum,maximum)
    return maximum
print(slidingWindow(arr,k))
