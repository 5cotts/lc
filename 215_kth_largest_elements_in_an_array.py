# https://leetcode.com/problems/kth-largest-element-in-an-array

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = heapq.nlargest(k, nums)
        return k_largest[-1]
