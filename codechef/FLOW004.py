# cook your dish here
t=int(input())
for i in range(t):
    a=int(input())
    l=a%10
    while(a>10):
        a=a//10
    ans=a+l
    print(ans)
