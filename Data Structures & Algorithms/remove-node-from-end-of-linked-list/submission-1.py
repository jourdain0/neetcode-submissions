# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Create a gap between left and right so that
        # right is n steps ahead of first
        while n > 0:
            right = right.next
            n -= 1
        
        # Now move both pointers until right reaches the end,
        # meaning that left.next will be the node to delete
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        
        return dummy.next
        