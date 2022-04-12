# https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def __init__(self) -> None:
        """init varz"""
        self._base_answer = [[]]
    
    # https://understanding-recursion.readthedocs.io/en/latest/08%20Power%20Set.html
    def _find_power_set(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return self._base_answer
        # Since we call this recursively, we need to grind `nums` down
        # to the base case until the answer is self._base_answer.
        # We achieve this by knocking off the last item in `nums` on each recursion.
        base = self._find_power_set(nums[:-1])
        operator = nums[-1:]
        ans = base + [b + operator for b in base]
        return ans
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self._find_power_set(nums)
