# https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    def _normalize_string(self, s: str) -> str:
        x = ""
        for char in s:
            if char.isascii() and char.isalnum():
                x += char.lower()
        return x
    
    def isPalindrome(self, s: str) -> bool:
        n = self._normalize_string(s)
        n_reversed = n[::-1]
        return n == n_reversed
