class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minPrice = 0, prices[0]

        for p in prices:
            res = max(res, p - minPrice)
            minPrice = min(minPrice, p)
        
        return res