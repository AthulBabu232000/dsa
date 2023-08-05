# convert binary to decimal 
def binaryToDecimal(a):
    rem=0
    i=0
    while(a!=0):
        rem=rem+(a%10)*2**i 
        i+=1 
        a=a//10
    return rem


# convert decimal to binary 
def decimalToBinary(dec):
    s=''
    while(dec!=0):
        r=dec%2 
        s+=str(r)
        dec=dec//2 
    s=s[::-1]
    if s=='':
        s='0'
    print(s)

def addBinary(a,b):
    x=binaryToDecimal(a)
    y=binaryToDecimal(b)
    output=x+y 
    result=decimalToBinary(output)
    return result 

finalOutput=addBinary(a=int(input("first binary number: ")),b=int(input("enter second binary number: ")))


