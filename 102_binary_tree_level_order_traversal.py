# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_to_nodes = defaultdict(list)
        q = [root, None]
        level = 0
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
    
    
        return [v for v in level_to_nodes.values()]
