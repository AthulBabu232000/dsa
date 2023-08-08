s="    34     234somestring324"
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'.
# Read this character in if it is either. This determines if the final result is negative or positive respectively. 
# Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. 
# The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
#  If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
# then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
def stringToInt(s):
    inputString=s.lstrip()
    resultString=""
    sign=""
    result=0
    signCount=0
    if len(inputString)==0:
        return result
    if inputString[0]=="+" or inputString[0]=="-":
        signCount+=1 
        sign+=inputString[0]
        if signCount==1:
            inputString=inputString[1:]
            print(inputString)
    if(len(inputString)>0):
        if(inputString[0].isdigit()):
            for i in inputString:
                if i.isdigit()==False:
                    break 
                resultString+=i 
        if len(resultString)>0:
            result=int(resultString)
        if sign == '-':
            result=-1*result 
        if result>(2**31)-1:
            result=(2**31)-1
        elif(result<-2**31):
            result=-2**31
    return result
    
output=stringToInt(s)
print(output)



