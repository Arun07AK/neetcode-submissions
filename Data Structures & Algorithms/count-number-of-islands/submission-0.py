class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        found=0
        seen=set()
        def dfs(r,c):
            if min(r,c)<0 or r>=len(grid) or          c>=len(grid[0]) or grid[r][c]=="0":
                return 
            if (r,c) in seen:
                return
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ((grid[i][j] =="1") and ((i,j) not in seen)):
                    found+=1
                    dfs(i,j)

        return found
            
                

        