# https://leetcode.com/problems/binary-tree-paths/

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self) -> None:
        """init varz"""
        self._join_char = "->"
    
    def _is_leaf(self, node: Optional[TreeNode]) -> bool:
        """The conditional for if a node is a leaf (i.e., is the end of a path, has no children)."""
        return not node.left and not node.right

    def _extend_path(self, orig_path: str, val: str) -> str:
        """Extend the provided path with the given value."""
        return self._join_char.join(
            [
                orig_path,
                val,
            ]
        )
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # No root node
        if not root:
            return []
        # No paths from root node
        elif self._is_leaf(root):
            return [str(root.val)]
        
        ans = []
        # The queue contains tuples of the node to it's path from root. We init the q with root. 
        q = deque([(root, str(root.val))])
        visited = set()
        while q:
            node, path = q.pop()
            print(path)
            
            if self._is_leaf(node):
                # In most cases, len(ans) == 2 because there should be two leaves,
                # one stemming from the left path from root and one stemming from the right path.
                ans.append(path)
            
            if node.left and node.left not in visited:
                q.append(
                    (
                        node.left,
                        self._extend_path(path, str(node.left.val)),
                    )
                )
            
            if node.right and node.right not in visited:
                q.append(
                    (
                        node.right,
                        self._extend_path(path, str(node.right.val)),
                    )
                )
            
            visited.add(node)
        
        return ans
