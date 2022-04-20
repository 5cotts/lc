# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def __init__(self) -> None:
        self._s: str = ""
        self.result: int = 0
    
    def _is_pallindrome(self, left: int, right: int) -> None:
        while (
            # These are inbounds checks.
            left >= 0 and right < len(self._s) 
            # and this is the pallindrome check
            and self._s[left] == self._s[right]
        ):
            left -= 1
            right += 1
            self.result += 1
    
    def countSubstrings(self, s: str) -> int:
        self._s = s
        for i in range(len(self._s)):
            self._is_pallindrome(i, i)
            self._is_pallindrome(i, i + 1)
        return self.result
