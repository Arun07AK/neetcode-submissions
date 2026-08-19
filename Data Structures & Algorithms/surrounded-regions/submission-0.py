class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        q=deque()
        seen=set()
        for r in range(rows):
            for c in [0,cols-1]:
                if board[r][c]=="O" and  (r,c) not in seen:
                    q.append((r,c))
                    seen.add((r,c))
        for c in range(0,cols):
            for r in [0,rows-1]:
                if board[r][c]=="O" and (r,c) not in seen:
                    q.append((r,c))
                    seen.add((r,c))

        def bfs(q,seen):
            while q:
                r,c=q.popleft()
                board[r][c]='T'
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if (nr,nc) not in seen and board[nr][nc]=="O" :
                            seen.add((nr,nc))
                            q.append((nr,nc))
        bfs(q,seen)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"
        