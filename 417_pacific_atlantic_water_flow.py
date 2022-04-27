# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Inspired by
# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/1903052/Python-DFS-from-Oceans

from typing import List, Set


class Solution:
    
    def __init__(self) -> None:
        self._grid = list()
        self._rows = 0
        self._cols = 0
        self._pacific_visited = set()
        self._atlantic_visited = set()
        
    def _get_neighbors(self, i: int, j: int) -> List[List[int]]:
        """Gets all neighbors that are in-bounds."""
        neighbors = list()
        # Left neighbor
        if j > 0:
            neighbors.append([i, j - 1])
        # Above neighbor
        if i > 0:
            neighbors.append([i - 1, j])
        # Right neighbor
        if j < self._cols - 1:
            neighbors.append([i, j + 1])
        # Below neighbor
        if i < self._rows - 1:
            neighbors.append([i + 1, j])
        return neighbors
    
    def _bfs(
        self,
        row: int,
        col: int,
        visited: Set[Tuple[int, int]],
        prev_cell_value: int,
    ) -> None:
        # If we've already visisted these coordinates, ignore them.
        # If the prev_cell_value is greater than the current cell's value,
        # water cannot flow between the two cells and we abort the traversal.
        if (row, col) in visited or prev_cell_value > self._grid[row][col]:
            return
        else:
            visited.add((row, col))
            for x, y in self._get_neighbors(row, col):
                self._bfs(x, y, visited, self._grid[row][col])
            
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self._grid = heights
        self._rows = len(heights)
        self._cols = len(heights[0])
        
        # Looks at the top and the bottom of the grid.
        for col in range(self._cols):
            # This traverses all cells that border the pacific at the top of the grid.
            self._bfs(0, col, self._pacific_visited, self._grid[0][col])
            # This traversesall cells that border the atlantic at the bottom of the gird.
            self._bfs(
                self._rows - 1,
                col,
                self._atlantic_visited,
                self._grid[self._rows - 1][col],
            )
        
        
        # Looks at left hand and right hand side of the grid.
        for row in range(self._rows):
            # This traverses over all cells that border the pacific on the left of the grid.
            self._bfs(row, 0, self._pacific_visited, self._grid[row][0])
            # This traverses all cells that border the atlantic on the right of the grid.
            self._bfs(
                row,
                self._cols - 1,
                self._atlantic_visited,
                self._grid[row][self._cols - 1],
            )
        
        return list(
            list(x)
            # "&" is set intersection.
            for x in self._pacific_visited & self._atlantic_visited
        )
