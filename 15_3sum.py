# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
                    
        answers = set()  
        
        for idx, num in enumerate(nums):
            l, u = idx + 1, len(nums) - 1
            while l < u:
                possible = (nums[l], nums[u], num)
                temp_sum = sum(possible)
                if temp_sum < 0:
                    l += 1
                elif temp_sum > 0:
                    u -= 1
                else:
                    l += 1
                    u -= 1
                    answers.add(possible)
                
        return [list(x) for x in answers]
