def sayFunc(s):
    count=1
    news=""
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            count+=1
        else:
            news+=str(count)+s[i-1]
            count=1
    news+=str(count)+s[-1]
    return news
def countSay(n):
    if n==1:
        return "1"
    return sayFunc(countSay(n-1))
output=countSay(30)
print(output)
