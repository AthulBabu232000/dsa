digit=6760
def sumDigit(n):
    if n//10==0:
        return n 
    return n%10+sumDigit(n//10)
result=sumDigit(digit)
print(result)

def printSum(i:int,s:int,n:int)->None:
    if i==n:
        s+=i 
        print(s)
        return 
    s+=i 
    printSum(i+1,s,n)




i:int=1 
s:int=0 
n:int=int(input("enter a number to find the sum: "))
printSum(i,s,n)
