from collections import deque 
class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        seen=set()
        q=deque()
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1

        if fresh ==0:
            return 0  
                    
        def addfruit(r,c):
            nonlocal fresh
            if(min(r,c)<0 or r>=rows or c>=cols or (r,c) in seen):
                return 
            if(grid[r][c]==0 or grid[r][c]==2):
                return
            seen.add((r,c))
            q.append([r,c])
            fresh-=1
        level=0
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    addfruit(r+dr,c+dc)
            level+=1
        return level if fresh ==0 else -1
                    



        