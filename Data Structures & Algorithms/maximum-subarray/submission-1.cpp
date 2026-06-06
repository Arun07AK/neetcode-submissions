class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int m = nums.size();
        vector<int> dp (m+1 , 0);
        int maxSum = nums[0];
        for(int i = 1;i<=m;i++)
        {
            dp[i]=max(nums[i-1],dp[i-1]+nums[i-1]);
            if (i == 1) maxSum = dp[i];
            else maxSum = max(maxSum, dp[i]);
        }
        return maxSum;


    }
};
