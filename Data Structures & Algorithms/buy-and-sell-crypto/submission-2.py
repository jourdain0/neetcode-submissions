class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("infinity")
        maxProfit = 0

        for price in prices:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)
        
        return maxProfit