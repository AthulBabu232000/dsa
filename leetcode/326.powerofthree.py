from math import log
def powerofThree(n):
    if n<=0:
        return False 
    return log(n,3).is_integer()
output=powerofThree(int(input("enter the number to check if the power of three or not: ")))
print(output)
