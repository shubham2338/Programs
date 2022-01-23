def median(nums1,nums2):
    s=nums1+nums2
    s=sorted(s)
    n=len(s)
    if n%2!=0:
        e=s[n//2]
    elif n%2==0:
        j=s[n//2]+s[(n//2)-1]
        e=j/2
    return "{0:f}".format(e)
n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
d=median(n1,n2)
print(d)
