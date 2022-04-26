# https://leetcode.com/problems/unique-paths-iii/

from typing import List


class Solution:
    def __init__(self) -> None:
        self.rows = 0
        self.cols = 0
        self.non_obstacle_squares = 0
        self.start_row = None
        self.start_col = None
        self.end_row = None
        self.end_col = None
        self.starting_value = 1
        self.ending_value = 2
        self.empty_value = 0
        self.obstacle_value = -1
        self.grid = list()
        self.answer = 0
    
    def backtracing(self, row: int, col: int, count: int) -> None:
        if (row, col) == (self.end_row, self.end_col):
            # When this is true, we know we have traversed every possible path.
            if count == self.non_obstacle_squares:
                self.answer += 1
            return
        
        # First step of backtracing, mark as visited.
        self.visited[row][col] = True
        
        # Now analyze all adjacent coordinates.
        for i, j in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
            if (
                # In-bounds
                0 <= i < self.rows and
                0 <= j < self.cols and
                # Not previously visisted
                not self.visited[i][j] and
                # valid square
                self.grid[i][j] != self.obstacle_value
            ):
                self.backtracing(i, j, count + 1)

        # Backtracing complete. Reset.
        self.visited[row][col] = False

    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        
        for row in range(self.rows):
            for col in range(self.cols):
                value = self.grid[row][col]
                if value != self.obstacle_value:
                    self.non_obstacle_squares += 1
                
                if value == self.starting_value:
                    self.start_row = row
                    self.start_col = col
                elif value == self.ending_value:
                    self.end_row = row
                    self.end_col = col
        
        self.backtracing(self.start_row, self.start_col, 1)
        return self.answer
