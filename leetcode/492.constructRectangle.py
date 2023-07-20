# make a rectangle with given area 
# width should not be larger than length 
# difference between width and length should be minimum as possible 
# return an array [L, W]
def find_factors(n):
    diff=n-1
    finalPair=list()
    finalPair.append([n,1])
    for i in range(1,n//2+1):
        pair=list()
        if n%i==0:
            pair.append(i)
            pair.append(n//i)
            if diff>abs(n//i - i):
                diff=abs(n//i - i)
                finalPair.append(pair)
    return finalPair
result=find_factors(122122)
print(result)

