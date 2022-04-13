# https://leetcode.com/problems/n-queens/

from typing import List

class Solution:
    def __init__(self) -> None:
        """init varz"""
        self._queen = "Q"
        self._empty = "."
        self._board = []
        self._n = None
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
    
    def _out_of_bounds(self, i: int, j: int) -> bool:
        """Determines if the provided (i, j) are 
        outside of the scope of the gameboard."""
        if i > self._n - 1 or j > self._n - 1:
            return True
        elif i < 0 or j < 0:
            return True
        else:
            return False
    
    def _is_queen(self, i: int, j: int) -> bool:
        return self._board[i][j] == self._queen
    
    def _is_valid_coords(self, i: int, j: int) -> bool:
        """Iterates over all possible nodes adjacent to the source node,
        asserting that the Queen is not in a direct line in any direction
        from the original (i, j) pair."""
        for i_modifier, j_modifier in self._directional_map.values():
            i_mod = i + i_modifier
            j_mod = j + j_modifier
            while not self._out_of_bounds(i_mod, j_mod):
                if self._is_queen(i_mod, j_mod):
                    return False
                else:
                    i_mod += i_modifier
                    j_mod += j_modifier
        return True
        
    def _materialize_board_with_vals(self) -> List[List[str]]:
        return [
            "".join([self._board[i][j] for j in range(self._n)]) for i in range(self._n)
        ]
    
    def _solve(self, i: int, ans: List[List[str]]) -> None:
        if i == self._n:
            ans.append(self._materialize_board_with_vals())
            return
        
        # Starting with provided row index (i), iterate over the boards column indicies (j).
        # Each time there is a valid (i, j), recurse on (i + 1).
        for j in range(self._n):
            if self._is_valid_coords(i, j):
                self._board[i][j] = self._queen
                self._solve(i + 1, ans)
                self._board[i][j] = self._empty
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Init the board, n, and the result
        self._board = [[self._empty for _ in range(n)] for _ in range(n)]
        self._n = n
        answer = []
        # Start with the row at index 0, back trace / recurse from there
        self._solve(0, answer)
        return answer
