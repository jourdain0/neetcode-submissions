# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        # Create gap
        while n > 0:
            right = right.next
            n -= 1
        
        # Find node to remove
        while right:
            left = left.next
            right = right.next
        
        # Remove the following node, which is the Nth node from end of list
        left.next = left.next.next

        return dummy.next