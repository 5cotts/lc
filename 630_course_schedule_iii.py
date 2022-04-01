# https://leetcode.com/problems/course-schedule-iii/submissions/

from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # courses[i] = [duration_i, lastDay_i]
        courses.sort(key=lambda x: x[1])
        day = 0
        taken = []
        for duration, last_day in courses:
            if day + duration <= last_day:
                day += duration
                heapq.heappush(taken, -duration)
            # The negative of a negative is a positive.
            # taken 0 is the max val from the heap.
            # Therefore, we are replacing the current max val, which is the smallest val.
            elif taken and -taken[0] > duration:
                day += duration + heapq.heapreplace(taken, -duration)
        return len(taken)
