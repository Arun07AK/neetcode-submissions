class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price_seen=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            max_profit=max(max_profit,prices[i]-min_price_seen)
            min_price_seen=min(min_price_seen,prices[i])
        return max_profit

        