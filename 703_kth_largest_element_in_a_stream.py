import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k        
        self._stream = nums
        
        # Empties the stream until we have the Kth
        # largest values remaining.
        heapq.heapify(self._stream)
        while len(self._stream) > self._k:
            heapq.heappop(self._stream)
        
        print(self._stream)

    def add(self, val: int) -> int:
        # If the stream is less than k, just push the value and let it get sorted.
        if len(self._stream) < self._k:
            heapq.heappush(self._stream, val)
        # If the value we are trying to add is larger than the current "min" value of the kth largest, then we replace it.
        elif val > self._stream[0]:
            heapq.heapreplace(self._stream, val)
        return self._stream[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
