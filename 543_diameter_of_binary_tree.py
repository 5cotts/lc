# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self) -> None:
        self._max_diameter = 0
    
    def _compute_max_diameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self._compute_max_diameter(root.left)
        right = self._compute_max_diameter(root.right)
        diameter = left + right
        
        # Re-assign the max diameter seen.
        self._max_diameter = max(self._max_diameter, diameter)
        
        # Traverse/consider only the greater path. 
        # Need to add one to account for the current root node.
        return 1 + max(left, right)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            # This function will recursively call until completion.
            self._compute_max_diameter(root)
        
        return self._max_diameter
