# https://leetcode.com/problems/validate-binary-search-tree/submissions/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        res = True
        
        def inorder(node):
            if node.left:
                inorder(node.left)
            
            nonlocal prev
            if prev is not None and node.val <= prev:
                nonlocal res
                res = False
                return
            
            prev = node.val
            
            if node.right:
                inorder(node.right)
    
        inorder(root)
        return res
