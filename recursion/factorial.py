factorialNo=7
def factorial(no):
    if no==0:
        return 1 
    if no==1:
        return 1 
    return no*factorial(no-1)

result=factorial(factorialNo)
print(result)