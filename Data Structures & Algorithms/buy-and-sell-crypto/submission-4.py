class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        res = 0

        for i in range(len(prices)):
            profit = prices[i] - minP
            res = max(res, profit)
            minP = min(minP, prices[i])
        
        return res