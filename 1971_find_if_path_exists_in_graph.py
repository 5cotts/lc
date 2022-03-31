# edges = [[0,1],[1,2],[2,0]]
#
#   0 1 2
# 0 0 1 1
# 1 1 0 1
# 2 1 1 0
#
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
#   0 1 2 3 4 5
# 0 0 1 1 0 0 0
# 1 1 0 0 0 0 0
# 2 1 0 0 0 0 0
# 3 0 0 0 0 1 1
# 4 0 0 0 1 0 1
# 5 0 0 0 1 0 1
# I experimented with the idea of using an adjacency matrix.

from collections import defaultdict
from typing import List

class Solution:
    
    def __init__(self) -> None:
        """Init varz"""
        self._node_to_children_map = defaultdict(list)
        self._visited_nodes = set()
    
    def _init_map(self, edges: List[List[str]]) -> None:
        """Populates the map for traversal."""
        # Need to add the left hand and right hand nodes as a key.
        for edge in edges:
            self._node_to_children_map[edge[0]].append(edge[1])
            self._node_to_children_map[edge[1]].append(edge[0])
    
    def _dfs(self, node: int) -> None:
        """Conducts traversal"""
        self._visited_nodes.add(node)
        children = self._node_to_children_map[node]
        for child in children:
            if child not in self._visited_nodes:
                self._dfs(child)
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """Conducts depth first search to determine if the destination node has been
        visited when starting traversal from the source."""
        self._init_map(edges)
        self._dfs(source)
        return destination in self._visited_nodes