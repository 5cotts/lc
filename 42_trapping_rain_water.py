# https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution:
    # This solution hits the time limit.
    # def trap(self, height: List[int]) -> int:
    #     units_of_trapped_rain = 0
    #     for i in range(1, len(height) - 1):
    #         left = max(height[:i])
    #         middle = height[i]
    #         right = max(height[i + 1:])
    #         water = min(left, right) - middle
    #         if water > 0:
    #             units_of_trapped_rain += water
    #     return units_of_trapped_rain
    
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        
        left_start = 0
        right_start = -1
        
        left[left_start] = height[left_start]
        for i in range(1, n):
            # At the current position, what is larger,
            # the current height or the previous height to the left.
            left[i] = max(height[i], left[i - 1])
        
        right[right_start] = height[right_start]
        # Decrement by 1, starting at n -2, and stop when i == -1.
        for i in range(n - 2, -1, -1):
            # At the current position, what is the larger,
            # the current height, or the next height to the right.
            right[i] = max(height[i], right[i + 1])
        
        for i in range(n):
            water =  min(left[i], right[i]) - height[i]
            if water > 0:
                total_water += water
                
        return total_water
