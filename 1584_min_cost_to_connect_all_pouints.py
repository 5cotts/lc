# https://leetcode.com/problems/min-cost-to-connect-all-points/
# https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1748076/Kruskal's-Algorithm
# https://www.programiz.com/dsa/kruskal-algorithm

from heapq import heappop, heappush
from typing import List, Tuple


class UnionFind:
    """
    A simple class containing methods to conduct a union find.
    More info:
        https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """
    
    def __init__(self, size: int) -> None:
        """init varz"""
        self._root = [i for i in range(size)]
        self._rank = [1 for _ in range(size)]
        self._count = size
    
    def _find(self, x: int) -> int:
        """Recusively finds the parent of x."""
        if x == self._root[x]:
            return self._root[x]
        
        self._root[x] = self._find(self._root[x])
        
        return self._root[x]
    
    def union(self, x: int, y: int) -> None:
        """Figures out the overlap between two nodes."""
        root_x = self._find(x)
        root_y = self._find(y)

        if root_x != root_y:
            rank_x = self._rank[root_x]
            rank_y = self._rank[root_y]
            
            if rank_x < rank_y:
                self._root[root_x] = root_y
            elif rank_y < rank_x:
                self._root[root_y] = root_x
            else:
                self._root[root_x] = root_y
                self._rank[root_y] += 1
            
            self._count -= 1
    
    def is_connected(self, x: int, y: int) -> bool:
        return self._find(x) == self._find(y)
    
    def get_count(self) -> int:
        return self._count


class Solution:
    def __init__(self) -> None:
        """init varz"""
        self._points = []
        self._min_heap = []
        self._max_edges = 0
        self._added_edges = 0
        self._cost = 0
    
    def _manhattan_distance(self, point_1: List[int], point_2: List[int]) -> int:
        x_i, x_j = point_1[0], point_2[0]
        y_i, y_j = point_1[1], point_2[1]
        return sum([abs(x_i - x_j), abs(y_i - y_j)])
    
    def _get_weighted_edges(self) -> List[Tuple[int, int, int]]:
        n = len(self._points)
        for i in range(n):
            for j in range(i + 1, n):
                heappush(
                    self._min_heap,
                    (
                        self._manhattan_distance(self._points[i], self._points[j]),
                        i,
                        j,
                    )
                )
                    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Init
        self._points = points
        self._get_weighted_edges()
        self._max_edges = len(self._points) - 1
        
        # Instantiate helper
        uf = UnionFind(len(self._points))

        while (
            self._min_heap and (
                self._added_edges != self._max_edges
            )
        ):            
            edge = heappop(self._min_heap)
            weight, i, j = edge
            if not uf.is_connected(i, j):
                uf.union(i, j)
                self._cost += weight
                self._added_edges += 1
                
        return self._cost
