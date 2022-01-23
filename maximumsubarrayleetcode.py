def subarrya(n):
    s=0
    mx=n[0]
    for i in n:
        if s<0: s=0
        s=s+i
        mx=max(mx,s)
    return mx
    

a=[2,4,-4,-6,3,1,2]
print(subarrya(a))