# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        u = len(numbers) - 1

        while l < u:
            tempSum = numbers[l] + numbers[u]
            if tempSum < target:
                l += 1
            elif tempSum > target:
                u -= 1
            else:
                return [l+1, u+1]
