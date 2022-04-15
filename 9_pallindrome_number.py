# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        parts = [bit for bit in str(x)]        
        parts.reverse()
        y = "".join(parts)
        return bool(str(x) == y)
    
    # Could you solve it without converting the integer to a string?
#      def isPalindrome ( self, x: int ) -> bool:
#         if x < 0:  # Smaller than zero, cannot be palindrome
#             return False

#         if x < 10:  # Single digit, is palindrome
#             return True

#         if x % 10 == 0:  # Ends with zero, cannot be palindrome
#             return False

#         # Reverse the given number
#         original = x
#         reverse = 0
#         while original > 0:
#             reverse = reverse * 10 + original % 10
#             original = original // 10
#             print(reverse, original)

#         # Check if the reversed number is equal to the original number
#         return x == reverse
