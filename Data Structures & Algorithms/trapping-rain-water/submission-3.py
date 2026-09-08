class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxL[0] = height[0]
        maxR = [0] * n
        maxR[n - 1] = height[n - 1]
        res = 0

        # Find the max height to the left of the current
        # bar (including the bar) and max height to the
        # right of the current bar (including the bar)
        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])
        
        # Calculate the max area by summing the water
        # that can be trapped at each bar using the
        # minimum of the tallest bars between the left
        # and right of the current bar subtracted by
        # the height of the current bar
        for i in range(n):
            res += min(maxL[i], maxR[i]) - height[i]
        
        return res