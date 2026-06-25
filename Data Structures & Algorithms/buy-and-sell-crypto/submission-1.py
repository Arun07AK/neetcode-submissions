class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>0:
                    max_val=prices[j]-prices[i]
                else:
                    max_val=0
                max_profit=max(max_profit,max_val)
        return max_profit
        