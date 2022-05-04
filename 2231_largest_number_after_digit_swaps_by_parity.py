# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity

class Solution:
    
    def is_even(self, num: int) -> bool:
        return num % 2 == 0
    
    def largestInteger(self, num: int) -> int:
        """
        It's just asking us to reverse the number, but in segments.
        Only reverse the odds and the evens, and bubble the largest
        nubmers to the front.
        """
        # Init varz
        num_array = [int(i) for i in str(num)]
        odd_nums, even_nums = [], []
        result = 0
        
        # Separate odd and even, then sort.
        for num in num_array:
            if self.is_even(num):
                even_nums.append(num)
            else:
                odd_nums.append(num)
        
        odd_nums.sort()
        even_nums.sort()
        
        # Reconstruct the result
        for num in num_array:
            if self.is_even(num):
                result = result * 10 + even_nums.pop()
            else:
                result = result * 10 + odd_nums.pop()
        
        return result
