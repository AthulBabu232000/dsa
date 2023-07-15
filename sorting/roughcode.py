def twoWayMerge(lst1, lst2):
    i=j=k=0
    arr=[0 for x in range(len(lst1)+len(lst2))]
    while(i<len(lst1) and j<len(lst2)):
        if(lst1[i]<lst2[j]):
            arr[k]=lst1[i]
            i+=1 
        else:
            arr[k]=lst2[j]
            j+=1 
        k+=1
    while(i<len(lst1)):
        arr[k]=lst1[i]
        i+=1 
        k+=1 
    while(j<len(lst2)):
        arr[k]=lst2[j]
        j+=1 
        k+=1 
    return arr
result=twoWayMerge([2,3,4],[9,6,5])
print(result)