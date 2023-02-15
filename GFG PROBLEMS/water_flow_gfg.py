def water_flow(self, mat, n, m):
    def valid(i,j,n,m,vis,p,mat):
        if i>=0 and j>=0 and i<n and j<m and vis[i][j]!=True and p<=mat[i][j]:
            return True
        return False
    vis=[[False for i in range(m)] for j in range(n)]
    q=[]
    for i in range(m):
        vis[0][i]=True
        q.append([0,i])
    for i in range(1,n):
        vis[i][0]=True
        q.append([i,0])
    indian=dict()
    while q:
        i,j=q.pop(0)
        vis[i][j]=True
        if (i,j) not in indian:
            indian[(i,j)]=True
        if valid(i+1,j,n,m,vis,mat[i][j],mat):
            vis[i+1][j]=True
            q.append([i+1,j])
            
        if valid(i,j+1,n,m,vis,mat[i][j],mat):
            vis[i][j+1]=True
            q.append([i,j+1])
            
        if valid(i-1,j,n,m,vis,mat[i][j],mat):
            vis[i-1][j]=True
            q.append([i-1,j])
            
        if valid(i,j-1,n,m,vis,mat[i][j],mat):
            vis[i][j-1]=True
            q.append([i,j-1])
    vi=[[False for i in range(m)] for j in range(n)]
    for i in range(n):
        q.append([i,m-1])
        vi[i][m-1]=True
    for j in range(m-1):
        q.append([n-1,j])
        vi[n-1][j]=True
    c=0
    while q:
        i,j=q.pop(0)
        vi[i][j]=True
        if (i,j) in indian and indian[(i,j)]==True:
            c+=1
        if valid(i+1,j,n,m,vi,mat[i][j],mat):
            vi[i+1][j]=True
            q.append([i+1,j])
            
        if valid(i,j+1,n,m,vi,mat[i][j],mat):
            vi[i][j+1]=True
            q.append([i,j+1])
            
        if valid(i-1,j,n,m,vi,mat[i][j],mat):
            vi[i-1][j]=True
            q.append([i-1,j])
            
        if valid(i,j-1,n,m,vi,mat[i][j],mat):
            vi[i][j-1]=True
            q.append([i,j-1])
    return c