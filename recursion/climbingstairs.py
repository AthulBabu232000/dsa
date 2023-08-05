def fibo(n):
    if n==1:
        return 1 
    if n==2:
        return 2 
    return fibo(n-1)+fibo(n-2)

def stairs(i,step):
    if i==step-1:
        return 1 
    elif i==step-2:
        return 2 
    return stairs(i+1,step)+stairs(i+2,step)
n:int=int(input("enter the final step no: "))

print("this problem is just like fibonacci sequence use loop bro: ")

def climbing(step:int)->int:
    i=1
    prev=1 
    curr=2 
    while(i<step):
        temp=curr 
        curr=curr+prev 
        prev=temp 
        i+=1
    return prev 

result:int=climbing(n)
print(result)

