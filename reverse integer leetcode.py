#using list method
'''
def reverse(a):
    if a>=(-2**31) and a<=(2**31)-1:
        b=str(a)
        if b[0]=='-' and b[-1]!='0':
            e=(b[:0:-1])
            d='-'+e
            return d
        elif b[-1]=='0' and b[0]=='-':
            e=(b[2:0:-1])
            d='-'+e
            return d
        elif b[-1]=='0' and b[0]!='-':
            e=b[-2::-1]
            return e
        else:
            e=b[::-1]
            return e
    else:
        return 0
a=int(input())
ans=reverse(a)
print(ans)

'''
#using stack method


def stack1(a):
    b=str(a)
    stack=[]
    if b=='0':
        return 0
    for i in b:
        stack.append(i)
    if stack[-1]=='0':
        while stack[-1]=='0':
            stack.pop()
    if stack[0]=='-':
        d=stack[:0:-1]
        d='-'+''.join(d)
    else:
        d=stack[::-1]
    j=''.join(d)
    j=int(j)
    return j
    if j<=(-2**31) or j>=(2**31)-1:
        return 0
    else:
        return j
a=int(input())
print(stack1(a))

