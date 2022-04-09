# https://leetcode.com/problems/clone-graph

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self) -> None:
        """Init varz"""
        self._cloned = dict()
    
    def _clone(self, node: 'Node') -> 'Node':
        # If we have already visisted this node,
        # we grab it's clone from the hash map.
        if node in self._cloned:
            return self._cloned[node]
        
        c = Node(node.val)
        self._cloned[node] = c
        for neighbor in node.neighbors:
            c.neighbors.append(self._clone(neighbor))
        
        return c
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self._clone(node) if node else None
