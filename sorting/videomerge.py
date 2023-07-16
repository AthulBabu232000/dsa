arr= [6, 5, 12, 10, 9, 1]

            #    6,5,12,10,9,1
            #        /  \
            #    6,5,12 10,9,1
            #     / \     / \
            #    6  5,12 10 9,1
            #        / \    / \ 
            #       5  12  9   1

def splitMerge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        print(left_half)
        print(right_half)
        splitMerge(left_half)
        splitMerge(right_half)
        i=j=k=0 
        while(i<len(left_half) and j<len(right_half)):
            if(left_half[i] < right_half[j]):
                arr[k]=left_half[i]
                k+=1
                i+=1
            else:
                arr[k]=right_half[j]
                k+=1
                j+=1   
        while(i<len(left_half)):
            arr[k]=left_half[i]
            k+=1 
            i+=1 
        while(j<len(right_half)):
            arr[k]=right_half[j]
            k+=1 
            j+=1 
        return arr 
    

       

result=splitMerge(arr)
print(result)