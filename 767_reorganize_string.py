# https://leetcode.com/problems/reorganize-string/

from collections import defaultdict
import heapq

class Solution:
    
    def __init__(self) -> None:
        """init varz"""
        self._char_freq = defaultdict(int)
    
    def _init_char_freq(self, s: str) -> None:
        for char in s:
            self._char_freq[char] += 1
    
    def _init_heapq(self, hq: list) -> None:
        for char, count in self._char_freq.items():
            # We use negative count because heapq is min heap by default
            heapq.heappush(hq, (-count, char))
        
    def reorganizeString(self, s: str) -> str:        
        heap_queue = []
        self._init_char_freq(s)
        self._init_heapq(heap_queue)
        
        answer = ""
        prev = ""
        while heap_queue or prev:
            print(heap_queue)
            if prev and not heap_queue:
                return ""
            
            count, char =  heapq.heappop(heap_queue)
            print(char)
            answer += char
            count += 1
            
            if prev:
                heapq.heappush(heap_queue, prev)
                prev = ""
                
            if count < 0:
                prev = (count, char)
            
        return answer
