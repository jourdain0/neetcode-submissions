class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxAmount = 0

        while l < r:
            currAmount = min(heights[l], heights[r]) * (r - l)
            maxAmount = max(maxAmount, currAmount)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxAmount