# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        q = [root, None]
        level_to_nodes = defaultdict(list)
        while q:
            node = q.pop(0)
            if node is None:
                level += 1
                q.append(None)
                if q[0] is None:
                    break
                else:
                    continue
            
            level_to_nodes[level].append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return [
            list(reversed(v)) if idx % 2 else v
            for idx, v in enumerate(level_to_nodes.values())
        ]
