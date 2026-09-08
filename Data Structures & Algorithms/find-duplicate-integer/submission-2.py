class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat nums as a linked list and finding a cycle
        slow = fast = 0
        
        # Find where slow and fast meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find where cycle starts, aka the duplicate number
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow