class Solution:
    def countPaths (self, n):
        # code here 
        m=10**9+7
        res=0
        for i in range(2,n+1):
            if i%2==0:
                res=(res%m*3%m)%m+3
            else:
                res=(res%m*3%m)%m-3
        return res%m