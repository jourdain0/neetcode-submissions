class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}

        for i in range(len(nums)):
            if target - nums[i] in have:
                return [have[target - nums[i]], i]
            have[nums[i]] = i