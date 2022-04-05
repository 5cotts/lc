# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to hold our list.
        dummy = pre = ListNode(0, head)
        
        # Iterate pre up to the left start
        for _ in range(left - 1):
            pre = pre.next
        
        # Now, reverse the portion between left and right.
        # new_pre will hold the of start reversed portion of the list
        new_pre = None
        # cur is the current node we are iterating on
        cur = pre.next
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = new_pre
            new_pre = cur
            cur = next_node
        
        # This iterates us past where we split the list for reversal.
        # `pre.next.next = cur` creates the tail of the list.
        # [<non-reversed-head>, <reversed_portion>, <non-reversed-tail>]
        # Index 0 is pre.
        # We are creating the entry at index 2 above.
        pre.next.next = cur
        
        # This creates the <reversed_portion> above.
        pre.next = new_pre
        
        # Return dummy.next because dummy itself is extraneous.
        return dummy.next
