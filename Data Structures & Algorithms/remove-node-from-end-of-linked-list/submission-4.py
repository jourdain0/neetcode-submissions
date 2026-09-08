# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        # Create gap between left and right
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Increment left and right until right reaches the end,
        # meaning left is now 1 behind the node to remove
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next

        return dummy.next