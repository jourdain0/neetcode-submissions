class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initilaize res with all 1's
        res = [1] * len(nums)

        # Get products of all nums left of i
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Multiply with products of all nums right of i
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res