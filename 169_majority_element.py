class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_to_num = {count: num for num, count in Counter(nums).items()}
        return count_to_num[max(count_to_num.keys())]
