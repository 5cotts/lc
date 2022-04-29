# https://leetcode.com/problems/number-of-1-bits/

from copy import deepcopy

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # Just because I don't like modifying variables in-place :)
        x = deepcopy(n)
        while x:
            # subtracting 1 changes the rightmost string of 0s to 1s,
            # and changes the rightmost 1 to a 0. If x originally had n
            # bits that were 1, then after only n iterations of this operation,
            # x will be reduced to zero.
            x &= x - 1
            count += 1
        return count
