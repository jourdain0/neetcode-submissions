# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Have a dummy before the start to handle edge cases
        dummy = ListNode(0, head)
        left, right = dummy, head

        # Create gap between left and right pointer
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Incrememnt pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
        
        # left.next will be the node to remove, so now remove in
        # and return the head
        left.next = left.next.next
        return dummy.next