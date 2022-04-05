# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List

class Solution:
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                max_area = max(max_area, (idx - i) * h)
                start = i
            stack.append((start, height))
        
        for idx, height in stack:
            area = (len(heights) - idx) * height
            max_area = max(max_area, area)
        
        return max_area
