# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    # Scott's original solution
    # (Instead of using a heap, also could have just appened all of the node values to a list
    # and then use the list sort method.)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        heapq.heapify(pq)
        for ll in lists:
            node = ll
            while node:
                curr_val = node.val
                heapq.heappush(pq, curr_val)
                node = node.next
        
        dummy = ListNode()
        ll_node = dummy
        while pq:
            val = heapq.heappop(pq)
            nxt = ListNode(val=val)
            ll_node.next = nxt
            ll_node = ll_node.next
        
        return dummy.next

    # A more optimized solution. Paired with Mukarram.
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         pq = []
#         for idx, head in enumerate(lists):
#             # For a weird case of lists = [[]].
#             if not head:
#                 continue
#             heapq.heappush(pq, (head.val, idx))
        
#         head = ListNode()
#         tail = head
#         while pq:
#             ll_val, ll_idx = heapq.heappop(pq)
            
#             if not pq:
#                 tail.next = lists[ll_idx]
#                 break
                
#             nxt_ll_val, _ = pq[0]
            
#             ll = lists[ll_idx]
#             node = ll
#             while node and node.val <= nxt_ll_val:
#                 nxt_node = node.next
#                 tail.next = ListNode(node.val)
#                 tail = tail.next
#                 node = nxt_node
            
#             lists[ll_idx] = node
#             if node is not None:
#                 heapq.heappush(pq, (node.val, ll_idx))
        
#         return head.next
