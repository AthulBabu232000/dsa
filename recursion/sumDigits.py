digit=6760
def sumDigit(n):
    if n//10==0:
        return n 
    return n%10+sumDigit(n//10)
result=sumDigit(digit)
print(result)