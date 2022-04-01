# https://leetcode.com/problems/task-scheduler/

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def __init__(self) -> None:
        """Init varz"""
        self._task_count_map = defaultdict(int)
    
    def _init_task_count_map(self, tasks: List[str]) -> None:
        for task in tasks:
            self._task_count_map[task] += 1
    
    def _init_heap_queue(self, hq: list) -> None:
        for task, count in self._task_count_map.items():
            # Use negative count because heaphq maintains a min heap but we want a max heap
            heapq.heappush(hq, (-count, task))
        
    def leastInterval(self, tasks: List[str], n: int) -> int:        
        num_cycles = n + 1
        heap_queue = []
        self._init_task_count_map(tasks)
        self._init_heap_queue(heap_queue)
        
        time = 0
        while heap_queue:
            tmp = []
            for _ in range(num_cycles):
                if heap_queue:
                    smallest_val = heapq.heappop(heap_queue)
                    tmp.append(smallest_val)
                        
            for count, task in tmp:
                # Once count is equal to zero, we know we have exhausted that task.
                # Therefore, we keep queueing until we hit that point.
                if count + 1 < 0:
                    heapq.heappush(heap_queue, (count + 1, task))
                    
            time += len(tmp) if not heap_queue else num_cycles
            
        return time
        
        

                    