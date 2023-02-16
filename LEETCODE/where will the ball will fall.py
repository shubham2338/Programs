class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def dfs(i,j):
            if i>=len(grid):
                return j
            if grid[i][j]==1  and j+1<len(grid[0]) and grid[i][j+1]==1 :
                return dfs(i+1,j+1)
            elif grid[i][j]==-1 and j-1>=0 and grid[i][j-1]==-1 :
                return dfs(i+1,j-1)
            elif grid[i][j]==1 and j>len(grid[0]):
                return -1
            else:
                return -1
            
        ans=[-1]*len(grid[0])
        r=len(grid)
        c=len(grid[0])
        for i in range(c):
            ans[i]=dfs(0,i)
        return ans
            
                