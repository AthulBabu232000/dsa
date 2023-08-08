s = "is2 sentence4 This1 a3"
def sortSentence(s):
    s_list=s.split(" ")
    s_list=[x[::-1] for x in s_list]
    s_list.sort()
    s_list=[x[1:][::-1] for x in s_list]
    return " ".join(s_list)
output=sortSentence(s)
print(output)
