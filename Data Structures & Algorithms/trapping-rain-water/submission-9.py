class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxL[0] = height[0]
        maxR = [0] * n
        maxR[n - 1] = height[n - 1]

        # Assign max value for left of i's
        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i])
        
        # Assign max values for right of i's
        for i in range(n - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])
        
        # Fill up the amount of water we can trap in each spot
        res = 0
        for i in range(n):
            res += min(maxL[i], maxR[i]) - height[i]
        
        return res
