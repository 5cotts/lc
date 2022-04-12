# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List
from copy import deepcopy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        def set_zeros(i: int, j: int) -> None:
            # This for loop sets the row to zero.
            for k in range(N):
                matrix[i][k] = 0
            
            # This for loop sets the col equal to zero.
            for row in matrix:
                row[j] = 0
        
        cpy = deepcopy(matrix)
        for i, row in enumerate(cpy):
            for j, col in enumerate(row):
                if cpy[i][j] == 0:
                    set_zeros(i, j)
