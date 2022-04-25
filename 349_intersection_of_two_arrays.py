# https://leetcode.com/problems/intersection-of-two-arrays/submissions/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Solution 1
        result = []
        dp = [0 for _ in range(0, 1001)]
        for num in nums1:
            dp[num] = 1
        
        for num in nums2:
            if dp[num] == 1:
                dp[num] += 1
                result.append(num)
        
        return result
        
        
        # Solution 2
#         nums1.sort()
#         nums2.sort()
        
#         n, m = len(nums1), len(nums2)
#         pointer_n, pointer_m = 0, 0
#         result = []
        
#         while pointer_n < n and pointer_m < m:
#             val_n = nums1[pointer_n]
#             val_m = nums2[pointer_m]
#             if val_n < val_m:
#                 pointer_n += 1
#             elif val_m < val_n:
#                 pointer_m += 1
#             else:
#                 if not result or val_n != result[-1]:
#                     result.append(val_n)
#                 pointer_n += 1
#                 pointer_m += 1
        
#         return result
