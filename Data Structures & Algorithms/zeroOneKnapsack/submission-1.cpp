class Solution {
public:
    int maximumProfit(vector<int>& profit, vector<int>& weight, int capacity) {
        int m = profit.size();

        vector<vector<int>> dp (m+1,vector<int>(capacity+1,0));
        for (int i = 1; i <=m;i++)
        {
            for(int w=1;w<=capacity;w++)
            {
                if(weight[i-1]<=w)
                {
                    dp[i][w]=max(dp[i-1][w],profit[i-1]+dp[i-1][w-weight[i-1]]);
                }
                else
                {
                    dp[i][w]=dp[i-1][w];
                }
            }
        }
        return dp[m][capacity];
    }
};
