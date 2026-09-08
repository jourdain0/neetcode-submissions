class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        neededNum = {}
        for i in range(len(nums)):
            if nums[i] in neededNum:
                return [neededNum[nums[i]], i]
            else:
                neededNum[target - nums[i]] = i