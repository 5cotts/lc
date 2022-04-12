# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:

    def __init__(self) -> None:
        """init varz"""
        self._answer = []
        self._candidates = []
    
    def _recursive_dfs(self, val: int, index: int, combination: List[int]) -> None:
        # If val is zero, we know the current combination is a potential answer.
        if val == 0:
            self._answer.append(combination)
        else:
            # Essentially running with two pointers here.
            # If we come across a candidate that is less than the current val,
            # we recurse on that candidate and all other possibilites until we
            # have exhausted it. Then we move on to the next candidate (by moving back to the original pointer).
            for k in range(index, len(self._candidates)):
                candidate = self._candidates[k]
                if candidate <= val:
                    self._recursive_dfs(val - candidate, k, combination + [candidate])
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self._candidates = candidates
        self._recursive_dfs(target, 0, [])
        return self._answer
