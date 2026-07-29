class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        cols=set()
        pos_diag=set()
        neg_diag=set()
        board=[["." for _ in range(n)]for _ in range(n)]
        def dfs(row,board):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            for col in range(0,n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                cols.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)
                board[row][col]="Q"
                dfs(row+1,board)
                board[row][col]="."
                cols.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
        dfs(0,board)
        return res
        