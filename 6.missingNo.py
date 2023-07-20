# return the missing number from an array given from 1 to N-1 
# N is the length of the array 
def missingNo(array,n):
    array.sort()
    if len(array)<n:
        zero=[0 for x in range(n-len(array))]
        array.extend(zero)
    for i in range(1,n+1):
        print(i,array[i-1])
        if(i!=array[i-1]):
            return i 
array=[1]
n:int=int(input("enter value for n: "))
result=missingNo(array,n)
print(result)