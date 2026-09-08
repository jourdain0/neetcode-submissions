class Solution:
    def trap(self, height: List[int]) -> int:
        # Have two arrays, one keeps track of max height
        # to the left of bar i, the other keeps track of
        # max height to the right of bar i. These will be
        # used to calculate amount of water you can trap
        # at a specific bar using the min of each array
        # minus the current height of bar i
        n = len(height)
        leftMax = [0] * n
        leftMax[0] = height[0]
        rightMax = [0] * n
        rightMax[-1] = height[-1]

        # Calculate max height to the left
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        # Calculate max height to the right
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        # Now sum up all the water you can trap and return
        maxWater = 0
        for i in range(n):
            maxWater += min(leftMax[i], rightMax[i]) - height[i]
        
        return maxWater