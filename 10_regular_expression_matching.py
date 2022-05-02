# https://leetcode.com/problems/regular-expression-matching

class Solution:
    
    def __init__(self) -> None:
        """init varz"""
        self._single_char_match = "."
        self._zero_or_more_of_preceding = "*"
        self._memo = dict()
    
    def _dp(self, i: int, j: int, string: str, pattern: str) -> bool:
        if (i, j) in self._memo:
            return self._memo[i, j]
        
        if j == len(pattern):
            ans = i == len(string)
        else:
            first_match = (
                i < len(string)
                and pattern[j] in [string[i], self._single_char_match]
            )
            
            if (
                # in-bounds
                j + 1 < len(pattern) and
                # wildcard
                pattern[j + 1] == self._zero_or_more_of_preceding
            ):
                ans = (
                    self._dp(i, j + 2, string, pattern) or
                    first_match and self._dp(i + 1, j, string, pattern)
                )
            else:
                ans = first_match and self._dp(i + 1, j + 1, string, pattern)
            
        self._memo[i, j] = ans
        return ans
    
    def isMatch(self, s: str, p: str) -> bool:
        return self._dp(0, 0, s, p)
