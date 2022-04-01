# https://leetcode.com/problems/lru-cache/

from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self._cache = {}
        self._capacity = capacity
        # The LRU key is at the back of this queue.
        # The MRU key is at the front of this queue.
        self._queue = deque()
            
    def get(self, key: int) -> int:
        value = -1
        if key in self._cache:
            value = self._cache[key]
            # This key was the most recently used.
            # If it's in the cache, it's in the queue
            # and we need to move it to the MRU position.
            self._queue.remove(key)
            self._queue.appendleft(key)
        return value
        
    def _at_capacity(self) -> bool:
        return len(self._cache) == self._capacity
        
    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            # This key was the most recently used.
            # If it's in the cache, it's in the queue
            # and we need to move it to the MRU position.
            self._queue.remove(key)
            self._queue.appendleft(key)
        else:
            if self._at_capacity():
                lru = self._queue.pop()
                del self._cache[lru]
            # If it wasn't in the cache,
            # the key still needs to be in the MRU position.
            self._queue.appendleft(key)
        
        # Finally, set the value in the cache.
        self._cache[key] = value

