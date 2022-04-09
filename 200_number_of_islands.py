# https://leetcode.com/problems/number-of-islands/submissions/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land_nodes = set()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                if val == "1":
                    land_nodes.add((i, j))
        
        num_islands = 0
        while land_nodes:
            nodes_to_consider = [land_nodes.pop()]
            while nodes_to_consider:
                i, j = nodes_to_consider.pop()
                for adj in [(i -1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                    if adj in land_nodes:
                        nodes_to_consider.append(adj)
                        land_nodes.remove(adj)
            num_islands += 1
        
        return num_islands
