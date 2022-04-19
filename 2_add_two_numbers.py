# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy var that will serve as our result set.
        # This is instantied with val=0, but if we return dummy.next,
        # we should have our linked list in order.
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            
            # If val > 10, we have to deal with the carry value from summation.
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)
            
            # Iterate through our linkedlists
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
