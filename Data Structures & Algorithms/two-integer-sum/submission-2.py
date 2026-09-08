class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousNums = {} # num --> index
        for i, num in enumerate(nums):
            if target - num in previousNums:
                return [previousNums[target - num], i]
            previousNums[num] = i