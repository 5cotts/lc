# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        # The base case is a set of all integers from 1 to n.
        base = set(range(1, n + 1))
        for row in matrix:
            if set(row) != base:
                return False
        for i in range(n):
            # The right hand operator is the column.
            if base != set(row[i] for row in matrix):
                return False
        return True
