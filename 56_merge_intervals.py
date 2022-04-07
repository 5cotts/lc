# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    
    def _check_overlap(self, interval1: List[List[int]], interval2: List[List[int]]) -> bool:
        """Checks if there is an overlap between the two provided intervals."""
        if interval1[0] <= interval2[0] <= interval1[1]:
            return True
        elif interval2[0] <= interval1[0] <= interval2[1]:
            return True
        else:
            return False
    
    def _merge_intervals(self, interval1, interval2) -> List[List[int]]:
        """Merges two intervals which have an overlap."""
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        # Sort the intervals and order it such that the 
        # intervals with the smallest start values are at the front.
        intervals.sort(reverse=True, key=lambda x: x[0])
        result = [intervals.pop()]

        while intervals:
            newInterval = intervals.pop()
            oldInterval = result.pop()

            # If there is any overlap, we merge the intervals.
            # We put this in a while loop to collapse merging 
            # that needs to occur across multiple intervals.
            # For example, if intervals looks like [[1,2], [3,4], [5,6], [7,8]]
            # and newInterval = [3, 7] we would need to merged [3,4], [5,6], and [7,8]
            # to create [[1,2] [3,8]]
            while self._check_overlap(newInterval, oldInterval):
                newInterval = self._merge_intervals(newInterval, oldInterval)
                if not result:
                    break
                oldInterval = result.pop()
            else:
                result.append(oldInterval)

            result.append(newInterval)

        return result
