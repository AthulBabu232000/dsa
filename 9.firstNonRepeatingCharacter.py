word="zxvczbtxyzvy"
# if char is not present in dict key:value char:index
# if char is present update dict key:value char:-1
# sort dict based on keys 
# iterate through dict if value is not -1 return corresponding key 
# question from geeks for geeks but it is not working on their site idk why
def findNon(w):
    wordDict=dict()
    for i in range(len(w)):
        if w[i] not in wordDict:
            wordDict[w[i]]=i 
        elif w[i] in wordDict:
            wordDict[w[i]]=-1
    wordDict=dict(sorted(wordDict.items(),key=lambda x:x[1]))
    for i in wordDict:
        if wordDict[i]!=-1:
            return i 
    return '$'
result=findNon(word)
print(result)