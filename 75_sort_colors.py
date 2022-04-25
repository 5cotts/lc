# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        
        for color in range(3):
            start_pointer = 0
            for prev_color_idx in range(color):
                start_pointer += counts[prev_color_idx]
            count = counts[color]
            for i in range(start_pointer, start_pointer + count):
                nums[i] = color
