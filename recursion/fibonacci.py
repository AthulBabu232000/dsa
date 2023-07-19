fiboNo=8
def fib(no):
    if no==1:
        return 0 
    if no==2:
        return 1
    return fib(no-1)+fib(no-2)
result=fib(fiboNo)
print(result)