from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows=len(heights)
        cols=len(heights[0])
        pq=deque()
        aq=deque()
        pv=set()
        av=set()

        for r in range(rows):
            if((r,0) not in pv):
                pq.append((r,0))
                pv.add((r,0))
            if ((r,cols-1)not in av):
                aq.append((r,cols-1))
                av.add((r,cols-1))
        for c in range(cols):
            if ((0,c) not in pv):
                pq.append((0,c))
                pv.add((0,c))
            if((rows-1,c) not in av):
                aq.append((rows-1,c))
                av.add((rows-1,c))

        def bfs(queue,seen):
            while queue:
                r,c=queue.popleft()

                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if (nr,nc) not in seen and heights[nr][nc]>=heights[r][c]:
                            seen.add((nr,nc))
                            queue.append((nr,nc))

        bfs(pq,pv)
        bfs(aq,av)
        return list(pv&av)
                            
                    