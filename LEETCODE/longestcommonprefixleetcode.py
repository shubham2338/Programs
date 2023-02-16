def longeststring(s):
    if len(s)==0: return ("")
    ml=len(s[0])
    for i in range(len(s)):
        ml=min(len(s[i]),ml)

    l = ""
    i=0
    while i<ml:
        char = s[0][i]
        for j in range(1,len(s)):
            if s[j][i] != char:
                return l
        l=l+char
        i=i+1
    return l

s=['shubham','shubh','shu','shubha']
d=longeststring(s)
print(d)
