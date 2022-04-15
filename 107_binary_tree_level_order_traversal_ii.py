# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import Optional, List

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        level_to_order = defaultdict(list)
        q = [root, None]
        while q:
            node = q.pop(0)
            if node is None:
                level += 1
                q.append(None)
                if q[0] is None:
                    break
                else:
                    continue
            
            level_to_order[level].append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return [v for v in list(reversed(level_to_order.values()))]
