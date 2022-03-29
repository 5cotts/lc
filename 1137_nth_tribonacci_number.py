# https://leetcode.com/problems/n-th-tribonacci-number/

from functools import cache

class Solution:
    
    @cache
    def tribonacci(self, n: int) -> int:        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            x = n - 3
            return self.tribonacci(x) + self.tribonacci(x+1) + self.tribonacci(x+2)

