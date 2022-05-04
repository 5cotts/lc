import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [
            x[1]
            for x in heapq.nsmallest(
                k,
                (
                    (sum(row), idx) for idx, row in enumerate(mat)
                ),
            )
        ]
