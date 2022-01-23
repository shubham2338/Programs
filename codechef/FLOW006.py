t=int(input())
while(t!=0):
    ans=0
    a=int(input())
    while(a!=0):
        c=a%10
        ans=ans+c
        a=a//10
    print(ans)
    t-=1
        
