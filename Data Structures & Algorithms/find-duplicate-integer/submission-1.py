class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Uses the finding the start of a cycle technique
        # with slow and fast pointers, treating the array
        # as a linked list
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow