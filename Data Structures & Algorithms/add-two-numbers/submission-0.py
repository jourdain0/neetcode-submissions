# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1, curr2 = l1, l2
        dummy = curr = ListNode()

        while curr1 and curr2:
            val = (curr1.val + curr2.val + carry) % 10
            carry = 1 if (curr1.val + curr2.val + carry) >= 10 else 0
            curr.next = ListNode(val)
            curr, curr1, curr2 = curr.next, curr1.next, curr2.next
        
        while curr1:
            val = (curr1.val + carry) % 10
            carry = 1 if (curr1.val + carry) >= 10 else 0
            curr.next = ListNode(val)
            curr, curr1 = curr.next, curr1.next
        
        while curr2:
            val = (curr2.val + carry) % 10
            carry = 1 if (curr2.val + carry) >= 10 else 0
            curr.next = ListNode(val)
            curr, curr2 = curr.next, curr2.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next