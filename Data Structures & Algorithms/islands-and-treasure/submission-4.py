from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        level=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    if min(r+dr,c+dc)<0 or r+dr >=rows or c+dc>=cols or grid[r+dr][c+dc]!=2147483647:
                        continue
                    grid[r+dr][c+dc]=level+1
                    q.append((r+dr,c+dc))
            level+=1


               
        

        