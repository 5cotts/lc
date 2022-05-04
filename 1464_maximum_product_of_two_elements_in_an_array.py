# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

import heapq

class Solution:
        
    def maxProduct(self, nums: List[int]) -> int:
        # Init varz
        _max = 0
        
        # Init priority queue
        pq = []
        heapq.heapify(pq)
        for n in nums:
            heapq.heappush(pq, n)
        
        # Return the two largest values from priortiy queue
        m, mm = heapq.nlargest(2, pq)
        _max = max(_max, (m - 1) * (mm - 1))
            
        return _max
