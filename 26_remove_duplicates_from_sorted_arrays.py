# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        if not nums:
            return k
        
        slower_pointer = 0
        for fast_pointer in range(1, k):
            # If the two values are not duplicates,
            # start trickling the faster pointer's value down to the lower index.
            # This will avoid duplicates and asserts that the elments at the end of the list which are not needed]
            # are not deleted.
            slow_val, fast_val = nums[slower_pointer], nums[fast_pointer]
            if slow_val != fast_val:
                slower_pointer += 1
                nums[slower_pointer] = nums[fast_pointer]
        
        return slower_pointer + 1
