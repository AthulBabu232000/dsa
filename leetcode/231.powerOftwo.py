# in this problem n is given: check if it is a power of two 
# every binary of two starts with one and it has only one one 
# every binary one behind the n i.e is n-1 is full of 1's 
# 4=>100 3=>11 similarlly 8=>1000 7=>111
def powerOfTwo(n):
    if n<=0:
        return False
    return n&n-1==0 
output=powerOfTwo(int(input("enter a number to find if it is a power of two: ")))
print(output)