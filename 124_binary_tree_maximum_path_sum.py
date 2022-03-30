# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self._max_sum = 0
    
    def sumAndTraverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.sumAndTraverse(root.left)
        right = self.sumAndTraverse(root.right)
        self._max_sum = max(
            self._max_sum,
            # We have to consider root.val in-case it has no children.
            root.val,
            root.val + left,
            root.val + right,
            # In-case it does pass through the root.
            root.val + left + right,
        )
        
        # The next path to traverse is the root.val (if it has no other children)
        # or it's right or left paths, depending on which one is greater.
        return max(root.val, root.val + left, root.val + right)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root:
            self._max_sum = root.val
            self.sumAndTraverse(root)
        return self._max_sum
        