class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        res = 0

        for p in prices:
            currP = p - minP
            res = max(res, currP)
            minP = min(minP, p)
        
        return res