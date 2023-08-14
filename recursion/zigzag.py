# Input 1 -> 1
# Output 1 -> 1 1 1

# Input 2 -> 2
# Output 2 -> 2 1 1 1 2 1 1 1 2

# Input 3 -> 3
# Output 3 -> 3 2 1 1 1 2 1 1 1 2 3 2 1 1 1 2 1 1 1 2 3

# def recursivePrinting(n:str,counter:int)->str:
#     if counter==3:
#         return n
#     n+=recursivePrinting(n,counter+1)
#     return n
# output=recursivePrinting("1",1)
# print(output)

def zigzagPrinting(n:str):
    if n=="1":
        return "111"
    s=n
    s+=zigzagPrinting(str(int(n)-1))
    s+=n
    s+=zigzagPrinting(str(int(n)-1))
    s+=n
    return s
output=zigzagPrinting("3")
print(output)


