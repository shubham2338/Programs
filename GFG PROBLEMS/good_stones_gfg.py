def goodStones(self, n, arr) -> int:
    #code here
    #Brute force
    '''
    res=0
    d=set()
    for i in range(n):
        h=i
        vis=[False]*n
        while not(vis[h]):
            vis[h]=True
            h=h+arr[h]
            if h<0 or h>=len(arr):
                res+=1
                break
    return res
    '''
    #using dynamic programming
    def fun(arr,i):
        if len(arr)<=i or i<0:
            return 2
        if dp[i]==1 or dp[i]==2 :
            return dp[i]
        dp[i]=1
        dp[i]=fun(arr,arr[i]+i)
        return dp[i]
        
    dp=[0]*n
    for i in range(n):
        if dp[i]==0:
            dp[i]=fun(arr,i)
    res=0
    for i in dp:
        if i==2:
            res+=1
    return res