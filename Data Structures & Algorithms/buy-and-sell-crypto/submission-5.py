class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Best time to buy and sell stock can be
        # calculated by using the lowest possible
        # buy price by day i and selling at that point.
        # So, when encountering a lower buy price, use that
        # for future sell points and use the maximum profit
        # at that point
        minPrice, maxProfit = prices[0], 0

        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        
        return maxProfit