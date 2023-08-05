def findPalindrome(string)->set:
    def callAroundPalindrome(left,right)->None:
        while(left>=0 and right<len(string) and string[left]==string[right]):
            palindromes.add(string[left:right+1])
            left=left-1 
            right=right+1 
    palindromes=set()
    for i in range(len(string)):
        callAroundPalindrome(i,i)
    return palindromes

def findLongestPalindrome(string)->str:
    findPalindromeResult=findPalindrome(string)
    stringResult=''
    for i in findPalindromeResult:
        if len(i)>len(stringResult):
            stringResult=i 
    return stringResult 


s:str=input("enter the string: ")
result=findLongestPalindrome(s)
print(result)


#  here goes my leetcode solution 
def longestPalindrome(self, s):
    palindromes=set() 
    for i in range(len(s)):
        left=i 
        right=i 
        while(left>=0 and right<len(s) and s[left]==s[right]):
            palindromes.add(s[left:right+1])
            left=left-1 
            right=right+1 
        left=i 
        right=i+1 
        while(left>=0 and right<len(s) and s[left]==s[right]):
            palindromes.add(s[left:right+1])
            left=left-1 
            right=right+1 
    result=''
    for i in palindromes:
        if len(i)>len(result):
            result=i 
    return result