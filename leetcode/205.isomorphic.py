s="badc"
t="baba"
# this isomorphic function is pretty good but memory limit exceeded in leetcode 
def isomorphic(s,t):
    if len(s)!=len(t):
        return False 
    concet=list(zip(s,t))
    tracker=dict() 
    for (i,j) in concet:
        if i not in tracker.keys():
            tracker[i]=j
        elif tracker[i]==j:
            continue 
        else:
            return False 
    print(tracker)
    if isomorphic(t,s)==True:
        return True 
    return False

def isIsomorphic( s, t):
    if len(s)!=len(t):
        return False 
    concet=list(zip(s,t))
    tracker=dict()
    for (i,j) in concet:
        if i not in tracker.keys():
            tracker[i]=j 
        elif tracker[i]!=j:
            return False
    print(tracker)
    tracker=dict()
    for(j,i)in concet:

        if j not in tracker.keys():
            tracker[j]=i 
            print(j,tracker[j])
        elif tracker[j]!=i:
            return False
    print(tracker)
    return True


def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    char_map = {}
    used_chars = set()

    for char1, char2 in zip(s, t):
        if char1 not in char_map:
            if char2 in used_chars:
                return False
            char_map[char1] = char2
            used_chars.add(char2)
        else:
            if char_map[char1] != char2:
                return False

    return True

# Test cases
print(isomorphic_strings("egg", "add"))  # Output: True
print(isomorphic_strings("foo", "bar"))  # Output: False
print(isomorphic_strings("paper", "title"))  # Output: True
print(isomorphic_strings(s,t))  # Output: True

    
