class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l=0
        r=1
        max_profit=0
        while(r<len(prices)):
            if prices[r]-prices[l]>0:
                max_profit=max(max_profit,prices[r]-prices[l])
            else :
                l=r
            r+=1
        return max_profit

        