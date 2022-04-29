# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n)
        if head is None or head.next is None:
            return None
        
        node = head
        v = set()
        while node is not None:
            if node in v:
                return node
            else:
                v.add(node)
                node = node.next
        
        return None
