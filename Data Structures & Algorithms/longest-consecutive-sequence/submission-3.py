class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if num - 1 in numsSet:
                continue
            currLength = 1
            while num + currLength in numsSet:
                currLength += 1
            longest = max(longest, currLength)
        
        return longest