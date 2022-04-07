# https://leetcode.com/problems/happy-number/submissions/

class Solution:
    def isHappy(self, n: int) -> bool:
        cycles = 0
        nums = [int(i) for i in str(n)]
        while nums:
            res = 0
            for num in nums:
                res += num**2
        
            if res == 1:
                return True
            else:
                nums = [int(i) for i in str(res)]
            
            cycles += 1
            if cycles > 10:
                return False
