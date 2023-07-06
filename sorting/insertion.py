arr=[2,7,4,1,3,6,5,0]
def insert(A,j):
    for i in range(j,0,-1):
        if A[i]<A[i-1]:
            temp=A[i]
            A[i]=A[i-1]
            A[i-1]=temp 
        else:
            break
for i in range(len(arr)):
    insert(arr,i)
print(arr)
# insertion sort have time complexity of O(n^2)
