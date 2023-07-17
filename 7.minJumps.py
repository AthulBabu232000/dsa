def minJumps(arr,n):
    pointer=0 
    count=0 
    while(pointer<n):
        if arr[pointer]==0:
            return -1
        else:
            pointer+=arr[pointer]
            count+=1 
        print(pointer)
    return count 
arr=[1,3,5,8,9,2,6,7,6,8,9]
arr1=[2,3,1,1,2,4,2,0,1,1]
n=11
result=minJumps(arr1,n)
print(result)
# this code is not right


class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        result=list()
        for i in range(N-1):
            current=A[i]
            pointer=i+1
            while(pointer<=N-1):
                if A[pointer]>current:
                    flag=0 
                    break
                else:
                    flag=1 
            if flag==1:
                result.append(A[i])
        result.append(A[N-1])
        return result
                    
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
        
