# https://leetcode.com/problems/two-sum/submissions/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        partial_to_idx = {}
        for idx, num in enumerate(nums):
            if num in partial_to_idx:
                return [partial_to_idx[num], idx]
            else:
                partial_to_idx[target - num] = idx
