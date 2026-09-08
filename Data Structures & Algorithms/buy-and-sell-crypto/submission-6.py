class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        res = 0

        for p in prices:
            res = max(res, p - minP)
            minP = min(minP, p)
        
        return res