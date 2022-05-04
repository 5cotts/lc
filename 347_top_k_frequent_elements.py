# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from collections import Counter
import heapq

class Solution:
    
    # The "Pythonic" solution IMO.
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     answer = []
    #     for num, _ in sorted(count.items(), key=lambda x: x[1], reverse=True):
    #         if len(answer) == k:
    #             break
    #         else:
    #             answer.append(num)
    # return answer
    
    # The "heapy" optimized way which meets the below criteria.
    # Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # Init heap
        pq = []
        for num, freq in count.items():
            heapq.heappush(pq, (freq, num))
            if len(pq) > k:
                heapq.heappop(pq)
        
        result = []
        while pq:
            result.append(heapq.heappop(pq)[1])
        
        return result
    
        # Or this one liner
        # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #     return [
        #         x[1] for x in heapq.nlargest(
        #             k, map(lambda x: (x[1], x[0]), Counter(nums).items())
        #         )
        #     ]
