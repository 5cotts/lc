# https://leetcode.com/problems/maximum-gap/submissions/

from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        max_difference = 0

        if n < 2:
            return max_difference
        
        nums.sort()
        for i in range(0, n - 1):
            # Because nums is sorted,
            # you are always guaranteed nums[i + 1] > nums[i].
            diff = nums[i + 1] - nums[i]
            max_difference = max(max_difference, diff)
        
        return max_difference
