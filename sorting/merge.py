def mergeSortHelper(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        arrL=arr[:mid]
        arrR=arr[mid:]

        mergeSortHelper(arrL)
        mergeSortHelper(arrR)

        i=j=k=0 
        while(i<len(arrL) and j<len(arrR)):
            if(arrL[i]<arrR[j]):
                arr[k]=arrL[i]
                i+=1
            else:
                arr[k]=arrR[j]
                j+=1 
            k+=1 
        while(i<len(arrL)):
            arr[k]=arrL[i]
            i+=1 
            k+=1 
        while(j<len(arrR)):
            arr[k]=arrR[j]
            j+=1 
            k+=1
    return arr
 
arr= [6, 5, 12, 10, 9, 1] 
mergeSortHelper(arr)
print(arr)   
for i in arr:
    print(i, end=" ")
print()
print(mergeSortHelper(arr))