def solve(self, N, K, G):
    f=N
    if len(G)==1:
        return G[0]
    else:
        i=K
        res=sum(G) 
        s=0
        while i<N:
            G.append(res)
            res+=res-G[i-K]
            i+=1
    return G[f-1]