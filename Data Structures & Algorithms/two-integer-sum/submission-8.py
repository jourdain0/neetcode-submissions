class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numNeeded = {}

        for i, num in enumerate(nums):
            if target - num in numNeeded:
                return [numNeeded[target - num], i]
            numNeeded[num] = i