class Solution:
    
    def _num_bits_in_x(self, x: int) -> int:
        count = 0
        for _ in range(32):
            
            if x & 1 > 0:
                count += 1
            
            x  = x >> 1

        return count
        
    def countBits(self, n: int) -> List[int]:
        answer = list()
        for i in range(n + 1):
            answer.append(self._num_bits_in_x(i))
        return answer
