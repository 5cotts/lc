# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
                
        # Instantiate a counter
        counter = 1
        
        # Assign the first two nodes, which we know will be in order of odd, even.
        node = head
        odd_head, even_head = node, node.next
        current_odd = odd_head
        current_even = even_head
        node = node.next.next
        
        # Increment by one beause we are already on the node at index 2
        counter += 2
        
        # Now, iterate through the nodes, tracking the odds and evens.
        while node:            
            if counter % 2 == 0:
                current_even.next = node
                current_even = node
            else:
                current_odd.next = node
                current_odd = node            
            
            node = node.next
            counter += 1
        
        # The even tail needs to be None because this node is already captured in the odds.
        current_even.next = None
        
        # Since odds come before even, the "next"
        # of the last odd must be the start of the evens.
        current_odd.next = even_head
        
        return head
