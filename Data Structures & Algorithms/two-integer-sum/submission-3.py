class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numNeeded = {}

        for i, n in enumerate(nums):
            if target - n in numNeeded:
                return [numNeeded[target - n], i]
            numNeeded[n] = i
    