class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        seen=set()
        res=0
        def dfs(r,c):
            if min(r,c)<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 0
            if (r,c) in seen :
                return 0
            seen.add((r,c))
            return 1+dfs(r,c+1)+dfs(r,c-1)+dfs(r+1,c)+dfs(r-1,c)
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    res=max(res,dfs(i,j))
        return res

        