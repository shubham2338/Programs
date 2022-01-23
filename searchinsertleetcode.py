# nums =[1,3,5,6], target = 5
#output = 2 if target 2 than output will be 1, target=7 than output=4

def search(a,t):
    l=0
    u=len(a)-1
    while(l<=u):
        m=(l+u)//2
        if a[m]==t:
            return m
        if a[m]<t:
            l=m+1
        else:
            u=m-1
    return l
        
        
a=[1,3,5,6]
n=7
print(search(a,n))
