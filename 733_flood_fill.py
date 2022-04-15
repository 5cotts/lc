# https://leetcode.com/problems/flood-fill/

from typing import List

class Solution:
    def _get_neighbors(self, i: int, j: int, grid: List[List[int]]):
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if i < len(grid) - 1:
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < len(grid[0]) - 1:
            neighbors.append((i, j + 1))
        return neighbors
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        q = [(sr, sc)]
        visited = set()
        while q:
            i, j = q.pop()
            image[i][j] = newColor
            for n_i, n_j in self._get_neighbors(i, j, image):
                if image[n_i][n_j] == oldColor:
                    if (i, j) not in visited:
                        q.append((n_i, n_j))
            visited.add((i, j))
        return image
