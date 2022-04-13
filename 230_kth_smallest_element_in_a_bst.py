# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    # in_order = left, root, right
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        ans = None
        
        def inorder_traversal(node):
            if node.left:
                inorder_traversal(node.left)
            
            nonlocal counter
            counter += 1
            if counter == k:
                nonlocal ans
                ans = node
                return

            if node.right:
                inorder_traversal(node.right)
                
        inorder_traversal(root)   
        return ans.val if ans else ans
