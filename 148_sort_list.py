# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def split(self, head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow
    
    def merge(self, left, right):
        dummy = tail = ListNode()
        while left or right:
            v1 = left.val if left else inf
            v2 = right.val if right else inf
            if v1 <= v2:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        return dummy.next
            

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        middle = self.split(head)
        
        left = self.sortList(head)
        right = self.sortList(middle)

        return self.merge(left, right)
