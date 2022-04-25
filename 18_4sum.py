# https://leetcode.com/problems/4sum/

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        results = set()
        
        # Since 1 <= nums.length <= 200 and we know we need to return quadruplets.
        if n < 4:
            return list(results)
        
        # Sort the list so that we can conduct a binary search.
        nums.sort()
        
        for pointer1 in range(n - 3):
            for pointer2 in range(pointer1 + 1, n - 2):
                left = pointer2 + 1
                right = n - 1
                                
                while right > left:
                    current_window = (
                        nums[pointer1],
                        nums[pointer2],
                        nums[left],
                        nums[right],
                    )
                    
                    s = sum(current_window)
                    
                    if s == target:
                        results.add(current_window)
                        
                    if s > target:
                        right -= 1
                    else:
                        left += 1
        
        return [list(x) for x in results]
