# https://leetcode.com/problems/max-area-of-island/

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Gather the coordinates of all of the islands.
        land_nodes = set()
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val == 1:
                    land_nodes.add((i, j))
        
        # Instantiate all of the possible areas with base case of 0.
        island_areas = [0]
        while land_nodes:
            nodes_to_consider = [land_nodes.pop()]
            local_area = 0
            while nodes_to_consider:
                i, j = nodes_to_consider.pop()
                # The node to consider is part of an island, thus we increment local area by one.
                local_area += 1
                for adj in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    # If an adjacent neighbor is also an island,
                    # we then add this to the queue and go back to the top of the while loop.
                    # We don't have to care about out-of-bounds coords here because they just
                    # won't be present in land_nodes.
                    if adj in land_nodes:
                        nodes_to_consider.append(adj)
                        land_nodes.remove(adj)
            
            # When we have exhausted all island neighbors, append the area we calculated for this island.
            island_areas.append(local_area)
        
        # The answer is the maximum area in this list.
        return max(island_areas)
