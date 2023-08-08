arr=[4,1,2,3]
# Sort the values at odd indices of nums in non-increasing order
# sort the values at even indices of nums in non-decreasing order
def arrange(arr):
    if len(arr)==1:
        return arr
    even=list()
    odd=list() 
    for i in range(len(arr)):
        if(i%2==0):
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    odd.reverse()
    result=list()
    for i in range(len(even)):
        result.append(even[i])
        if i<len(odd):
            result.append(odd[i])
    return result
output=arrange(arr)
print(output)