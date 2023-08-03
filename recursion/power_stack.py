def power_stack(n,x)->int:
    if n==1:
        return x
    return x*power_stack(n-1,x)

n:int=int(input("enter no to find the power: "))
x:int=int(input("enter the base: "))
result=power_stack(n,x)
print(result)
print(6**4)