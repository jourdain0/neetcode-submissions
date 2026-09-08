class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP, res = prices[0], 0

        for p in prices:
            res = max(res, p - minP)
            minP = min(minP, p)
        
        return res