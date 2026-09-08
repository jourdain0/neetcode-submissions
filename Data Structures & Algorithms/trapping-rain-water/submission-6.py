class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxL[0] = height[0]
        maxR = [0] * n
        maxR[n - 1] = height[n - 1]
        res = 0

        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])
        
        for i, h in enumerate(height):
            res += min(maxL[i], maxR[i]) - h

        return res