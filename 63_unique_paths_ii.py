# https://leetcode.com/problems/unique-paths-ii

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid) - 1
        COLS = len(obstacleGrid[0]) - 1

        def dfs(row, col, memo=dict()):
            if row < 0:
                return 0
            elif col < 0:
                return 0
            elif obstacleGrid[row][col] == 1:
                return 0
            elif row == 0 and col == 0:
                return 1

            if (row, col) in memo:
                return memo[(row,col)]
            else:
                down = dfs(row - 1, col)
                right = dfs(row, col - 1)
                memo[(row, col)] = down + right
                return memo[(row, col)]
    
        return dfs(ROWS, COLS)
