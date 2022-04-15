# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def _is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        # Base case
        if self._is_palindrome(s):
            return True
        
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                # Everything but the value at i
                slice1 = s[:l] + s[l+1:]
                # Everything but the value at n
                slice2 = s[:r] + s[r+1:]
                return any(self._is_palindrome(x) for x in [slice1, slice2])
            else:
                l += 1
                r -= 1

        return False
