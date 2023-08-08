s="hello"
def reverse(s):
    if len(s)==0:
        return 
    reverse(s[1:])
    print(s[0],end="")
reverse(s)

# Stack implementation of printing reverse a string
# ===================================================
# reverse("")          s=""          return
# reverse("o")         s="o"         print(s[0]) falls back to lower stack
# reverse("lo")        s="lo"        print(s[0]) falls back to lower stack
# reverse("llo")       s="llo"       print(s[0]) falls back to lower stack
# reverse("ello")      s="ello"      print(s[0]) falls back to lower stack
# reverse("hello")     s="hello"     print(s[0]) falls back to main()
# main()               s="hello"     
