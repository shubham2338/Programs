def roman(s):
    dic1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    cur=0
    pre=0
    for i in range(len(s)):
        cur=dic1[s[i]]
        if cur>pre:
            total=total+cur-2*pre
        else:
            total=total+cur
        pre=cur
    return total
s=roman("XII")
print(s)
