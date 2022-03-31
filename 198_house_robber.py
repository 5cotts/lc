from typing import List

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        """Rob the homes. The amount you get from each home is represented
        by the integer in the list. You cannot rob two adjacent homes,
        else the police will come."""
        
        # sum1 is the previous sum pointer
        # sum2 is the previous, previous sum pointer 
        sum1 = sum2 = 0
        for n in nums:
            amt = max(n + sum1, sum2)
            sum1, sum2 = sum2, amt
        return sum2
