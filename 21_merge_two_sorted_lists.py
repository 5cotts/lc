# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            temp_node=None
            
            if list1.val <= list2.val:
                temp_node = list1
                temp_node.next = self.mergeTwoLists(temp_node.next, list2)
            else:
                temp_node = list2
                temp_node.next = self.mergeTwoLists(list1, temp_node.next)

            return temp_node
