def inSequence(A, B, C):
    # code here
    if C==0: 
        if A==B:
            return 1
        else: return 0
    n=(B-A)/C+1
    if n<=0:
        return 0
    else:
        if n*10%10==0:
            return 1
        return 0
a,b,c=map(int,input().split())
print(inSequence(a,b,c))