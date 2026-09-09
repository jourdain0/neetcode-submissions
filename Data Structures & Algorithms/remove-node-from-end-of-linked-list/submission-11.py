# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # Dummy node in case of the node we want to remove is head
        left, right = dummy, head

        # Create gap between left and right corresponding to n
        while n > 0:
            right = right.next
            n -= 1
        
        # Now move left until right reaches end, next node will be the
        # node we want to removeNthFromEnd
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
        