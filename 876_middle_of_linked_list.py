# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = fast = head
        
        # Iterate until fast reaches the end of the list.
        # Slow should be at the middle when this happens.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
