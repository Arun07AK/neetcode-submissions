class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[["." for _ in range(n)]for _ in range(n)]
        def dfs(row,board):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            for col in range(0,n):
                if is_valid(row,col,board):
                    board[row][col]="Q"
                    dfs(row+1,board)
                    board[row][col]="."

        def is_valid(row,col,board):
            #checking if there is any in the same column in any previous/upper row
            for r in range(row):
                if board[r][col]=="Q":
                    return False
            #checking diagonally top left
            r=row-1
            c=col-1
            while (r>=0 and c>=0):
                if board[r][c]=="Q":
                    return False
                r-=1
                c-=1
            #checking diagonally top right
            r=row-1
            c=col+1
            while(r>=0 and c<n):
                if board[r][c]=="Q":
                    return False
                r-=1
                c+=1
            return True
        dfs(0,board)
        return res
        