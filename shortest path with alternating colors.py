class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        r=collections.defaultdict(list) 
        b=collections.defaultdict(list) 
        #adjacency list 
        for s,d in redEdges:
            r[s].append(d)
        for s,d in blueEdges:
            b[s].append(d) 
        res=[-1]*n
        res[0]=0
        q=[]
        q.append([0,0,None]) # [source,length,colors]
        vis=set()
        vis.add((0,None)) 
        while q:
            n,l,c=q.pop(0)
            if res[n]==-1:
                res[n]=l
            if c!='R':
                for nb in r[n]:
                    if (nb,'R') not in vis:
                        vis.add((nb,'R'))
                        q.append([nb,l+1,'R'])
            if c!='B':
                for nb in b[n]:
                    if (nb,'B') not in vis:
                        vis.add((nb,'B'))
                        q.append([nb,l+1,'B'])
        return res