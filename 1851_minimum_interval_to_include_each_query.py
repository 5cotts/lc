# https://leetcode.com/problems/minimum-interval-to-include-each-query/

from collections import deque
import heapq
from typing import List

class Solution:
    def _get_interval_size(self, interval) -> int:
        return (interval[1] - interval[0]) + 1
    
    # This solution times out.
    # def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    #     intervals.sort(reverse=True, key=lambda x: x[0])
    #     result = []
    #     for query in queries:
    #         smallest_interval = None
    #         for interval in intervals:
    #             if interval[0] <= query <= interval[1]:
    #                 size = self._get_interval_size(interval)
    #                 if smallest_interval is not None:
    #                     smallest_interval = min(size, smallest_interval)
    #                 else:
    #                     smallest_interval = size
    #         result.append(-1 if smallest_interval is None else smallest_interval)
    #     return result
    
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Map queries from small to large with their corresponding index.
        pq = deque(sorted([(query, idx) for idx, query in enumerate(queries)]))
                
        # Init state of result to all -1.
        result = [-1] * len(queries)
        
        # Sort intervals by left, right, size
        intervals_with_score = deque(sorted(
            [
                (interval[0], interval[1], self._get_interval_size(interval))
                for interval in intervals
            ]
        ))
        
        # Prepare the candidate array
        candidates = []
        
        
        while pq:
            query, idx = pq.popleft()
            
            # Start by investigating if query is >= than left. 
            while intervals_with_score and query >= intervals_with_score[0][0]:
                # If query >= left, we remove this from the queue because we have considered it.
                left, right, score = intervals_with_score.popleft()
                # If query >= left and <= right, we push it to the heap
                # as a candidate because the query is in the interval.
                if query <= right:
                    # Change the order here because we want to maintain a min heap by score
                    heapq.heappush(candidates, (score, left, right))
            
            while candidates:
                score, left, right = heapq.heappop(candidates)
                if query <= right:
                    result[idx] = score
                    heapq.heappush(candidates, (score, left, right))
                    break
        
        return result
