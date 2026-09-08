class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxAmount = 0

        while l < r:
            maxAmount = max(min(heights[l], heights[r]) * (r - l), maxAmount)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxAmount