# https://leetcode.com/problems/powx-n/submissions/

class Solution:
    # This solution times out.
    # def myPow(self, x: float, n: int) -> float:
    #     res = 1
    #     for _ in range(abs(n)):
    #         res *= x         
    #     return res if n > 0 else 1/res
    
    # https://en.wikipedia.org/wiki/Exponentiation_by_squaring
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        elif n == 0:
            return 1
        elif n % 2 == 0:
            return self.myPow(x*x, n/2)
        elif n % 2 != 0:
            return x * self.myPow(x*x, (n-1)/2)
        