s = "abcdbcgranitegttdbcgranitesfor"

def longest(s):
    start=0 
    end=start 
    str_obt=s[start:end+1]
    tracker=dict()
    while(end<len(s)):
        if(s[end] in tracker.keys()):
            start=max(start,tracker[s[end]]+1)
        tracker[s[end]]=end 
        if(len(str_obt)<len(s[start:end+1])):
            str_obt=s[start:end+1]
        end+=1
    print(tracker)
    return str_obt 
output=longest(s)
print(output)

        



