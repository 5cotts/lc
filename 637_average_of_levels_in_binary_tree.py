# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
from typing import List, Optional
from statistics import mean

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Need to do a BFS
        level = 0
        level_values = defaultdict(list)
        # Use None to dictate the end of a level.
        q = [root, None]
        while q:
            # For BFS, pop from the left-hand side and append top the right hand side.
            node = q.pop(0)
            
            # You know you've reached the end of the previous level here.
            if node is None:
                level += 1
                q.append(None)
                # If the next node is the None you just appended, then this is the end of the graph.
                if q[0] is None:
                    break
                else:
                    # Continue to the next level of the tree 
                    continue
            
            level_values[level].append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        level_averages = []
        for _, values in level_values.items():
            level_averages.append(mean(values))
        return level_averages
