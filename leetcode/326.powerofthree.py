# so here i used is_integer() to check if it is an integer or not 
# i faced an issue with the number 243 log(243,3)=>4.99999999999
# first fix i used to round the number to 4 decimal places 
# i made 5 submissions all failed only round(log(n,3),10)
# only 10 decimal places works well
from math import log
def powerofThree(n):
    if n<=0:
        return False 
    print(log(n,3))
    prev=round(log(n,3),10)
    print(prev)
    return prev.is_integer()
output=powerofThree(int(input("enter the number to check if the power of three or not: ")))
print(output)
