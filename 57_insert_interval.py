# https://leetcode.com/problems/insert-interval

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for idx, interval in enumerate(intervals):
            if (
                any(x in range(interval[0], interval[1] + 1) for x in newInterval) or
                any(x in range(newInterval[0], newInterval[1] + 1) for x in interval)
            ):
                start = interval[0] if interval[0] < newInterval[0] else newInterval[0]
                end = interval[1] if interval[1] > newInterval[1] else newInterval[1] 
                newInterval = [start, end]
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                result.extend(intervals[idx:])
                break
            else:
                result.append(interval)
        
        if not result or result[-1][1] < newInterval[0]:
            result.append(newInterval)

        return result
