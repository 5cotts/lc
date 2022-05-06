class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        middle_idx = len(nums) // 2
        # even amount of nums
        if len(nums) % 2 == 0:
            # Single slash to get float
            return sum([nums[middle_idx], nums[middle_idx - 1]]) / 2
        # odd amount of nums
        else:
            return float(nums[middle_idx])
