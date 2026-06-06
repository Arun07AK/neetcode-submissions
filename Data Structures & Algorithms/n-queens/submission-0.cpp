class Solution {
    vector<int> column;
    vector<vector<string>> result;
    
public:
    vector<vector<string>> solveNQueens(int n) {
        column.assign(n+1,0);
        Nqueens(1,n);
        return result;
        
    }
    
    void Nqueens(int k,int n)
    {
        if (k==n+1)
        {
            vector<string> board ;
            for(int r=1;r<=n;r++)
            {
                string row(n,'.');
                row[column[r]-1]='Q';
                board.push_back(row);
            }
            result.push_back(board);
            return ;
        }
        for(int j=1;j<=n;j++)
        {
           if(place(j,k))
           {
                column[k]=j;
                Nqueens(k+1,n);
                column[k]=0;
           }

            
        }
    }
    bool place (int i , int k)
    {
        for (int j=1;j<k;j++)
        {
            if(column[j]==i)
                return false;
            if(abs(column[j]-i)==abs(j-k))
                return false;

        }
        return true;
    }
};
