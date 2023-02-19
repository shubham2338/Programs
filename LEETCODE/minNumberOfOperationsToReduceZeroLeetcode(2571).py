class Solution:
    def minOperations(self, n: int) -> int:
        res=0
        for i in range(32):
            h=bin(n+2**i)
            b=bin(n)
            if h.count('1')<=b.count('1')-1:
                n=n+(2**i)
                res+=1
        c=bin(n)
        return res+c.count('1')
        
        
        