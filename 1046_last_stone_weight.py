import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        heapq.heapify(pq)
        for s in stones:
            heapq.heappush(pq, -s)
        
        while len(pq) > 1:
            # Heap properties assert that x<=y
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)
            # The stone is smashed to bits and eliminated from our possibilities!
            if x == y:
                continue
            else:
                new_stone_weight = y - x
                heapq.heappush(pq, -new_stone_weight)
        
        return -pq[0] if pq else 0
