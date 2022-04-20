# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    
    def __init__(self) -> None:
        self._s: str = ""
        self.result: str = ""
    
    def _is_pallindrome(self, left: int, right: int):
        while left >= 0 and right < len(self._s):
            # Then we know we are not dealing with a pallindrome.
            if self._s[left] != self._s[right]:
                break

            left -= 1
            right += 1
            
            # If this pallindrome is larger than the current,
            # then we have a new result.
            num_characters = right - left
            if num_characters > len(self.result):
                self.result = self._s[left + 1 : right]

    def longestPalindrome(self, s: str) -> str:
        self._s = s
        for i in range(len(self._s)):
            self._is_pallindrome(i, i)
            self._is_pallindrome(i, i + 1)
        return self.result
