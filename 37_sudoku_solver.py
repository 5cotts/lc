# https://leetcode.com/problems/sudoku-solver/

from typing import List

class Solution:
    
    def __init__(self) -> None:
        """init varz"""
        # For any given (i, j) in the matrix, apply these (i_mod, j_mod)
        # to the original (i, j) in order to find the point in the matrix
        # that corresponds to the direction. For example, "nw" is the upper right,
        # or northwest coordinate from the original coordinate.
        self._directional_map = {
            "nw": (-1, -1),
            "n": (-1, 0),
            "ne": (-1, 1),
            "w": (0, -1),
            "e": (0, 1),
            "sw": (1, -1),
            "s": (1, 0),
            "se": (1, 1),
        }
        self._n = 9
        self._board = []
        self._empty = "."
        self._emptys = []
        self._remove = True
        self._rows = [set() for _ in range(self._n)]
        self._cols = [set() for _ in range(self._n)]
        self._grids = [set() for _ in range(self._n)]
    
    def _out_of_bounds(self, i: int, j: int) -> bool:
        """Determines if the provided (i, j) are 
        outside of the scope of the gameboard."""
        if i > self._n - 1 or j > self._n - 1:
            return True
        elif i < 0 or j < 0:
            return True
        else:
            return False
    
    def _all_vertical(self, i: int, j: int):
        """Grabs all the vertical coordinates and their values from the the input (i, j)."""
        north_modifier = self._directional_map["n"]
        south_modifier = self._directional_map["s"]
        for i_modifier, j_modifier in [north_modifier, south_modifier]:
            i_mod = i + i_modifier
            j_mod = j + j_modifier
            while not self._out_of_bounds(i_mod, j_mod):
                yield self._board[i_mod][j_mod]
                i_mod += i_modifier
                j_mod += j_modifier
    
    def _all_horizontal(self, i: int, j: int):
        res = {}
        west_modifier = self._directional_map["w"]
        east_modifier = self._directional_map["e"]
        for i_modifier, j_modifier in [west_modifier, east_modifier]:
            i_mod = i + i_modifier
            j_mod = j + j_modifier
            while not self._out_of_bounds(i_mod, j_mod):
                yield self._board[i_mod][j_mod]
                i_mod += i_modifier
                j_mod += j_modifier
    
    def _gen_3x3_grids(self, i: int, j: int):
        grids = [set() for _ in range(self._n)]
        for i, row in enumerate(self._board):
            for j, col in enumerate(row):
                val = self._board[i][j]
                idx = (i // 3) * 3 + (j // 3)
                grids[idx].add(val)
        return grids

            
    def _is_valid_coords(self, i: int, j: int, value: str) -> bool:
        grid_idx = (i // 3) * 3 + (j //3)
        all_neighbors = (
            self._gen_3x3_grids(i, j)[grid_idx] |
            set(self._all_vertical(i, j)) | 
            set(self._all_horizontal(i, j))
        )
        
        if value in all_neighbors:
            return False
        else:
            return True
    
    def _find_all_empty_coords(self):
        for i in range(self._n):
            for j in range(self._n):
                if self._board[i][j] == self._empty:
                    yield (i, j)
    
    def _are_valid_coords(self, i, j, val):
        grid_idx = (i // 3) * 3 + (j // 3)
        if val in self._rows[i] or val in self._cols[j] or val in self._grids[grid_idx]:
            return False
        else:
            return True
                    
    def _backtrace(self, start: int):
        if start == len(self._emptys):
            self._remove = False
            return
        
        row_idx, col_idx = self._emptys[start][0], self._emptys[start][1]
        # Iterate over 1-9.
        for i in range(1, self._n + 1):
            desired_val = str(i)
            # If it's valid, then we set it for real and continue iterating.
            if self._are_valid_coords(row_idx, col_idx, desired_val):
                self._board[row_idx][col_idx]= desired_val
                self._rows[row_idx].add(desired_val)
                self._cols[col_idx].add(desired_val)
                grid_idx = (row_idx // 3) * 3 + (col_idx // 3)
                self._grids[grid_idx].add(desired_val)
                self._backtrace(start + 1)
                if self._remove:
                    self._board[row_idx][col_idx] = self._empty
                    self._rows[row_idx].remove(desired_val)
                    self._cols[col_idx].remove(desired_val)
                    grid_idx = (row_idx // 3) * 3 + (col_idx // 3)
                    self._grids[grid_idx].remove(desired_val)
                    
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._board = board
        
        for i in range(self._n):
            for j in range(self._n):
                value = self._board[i][j]
                if value == self._empty:
                    self._emptys.append((i, j))
                    continue
                else:
                    self._rows[i].add(value)
                    self._cols[j].add(value)
                    grid_idx = (i // 3) * 3 + (j // 3)
                    self._grids[grid_idx].add(value)
                
        self._backtrace(0)
