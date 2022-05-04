# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from collections import Counter

class Solution:
    
    def __init__(self) -> None:
        """init varz"""
        # Since we are dealing with groups of 2,
        # and they are all lowercase English characters,
        # we need a 26x26 grid.
        self._map = [
            [0] * (ord("z") - ord("a") + 1)
            for _ in range(ord("z") - ord("a") + 1)
        ]
    
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        ## Situation 1: Where both letters are different (e.g., ["lc"])
        ## If palindrome exists, then we know we can expand ans by 4 because
        ## ["lc"] and ["cl"] are the same! Known as mirror words.
        for char1, char2 in words:
            ord1 = ord(char1) - ord("a")
            ord2 = ord(char2) - ord("a")
            # Look for palindromes in the map by looking for the
            # "reverse" (e.g., [ord2, ord1] instead of [ord1, ord2])
            # coordinates in the map.
            if self._map[ord2][ord1]:
                ans += 4
                self._map[ord2][ord1] -= 1
            # If no palindrome, simply enter the coordinates.
            else:
                self._map[ord1][ord2] += 1
        
        ## Situation 2: Where both letters are the same (e.g., ["gg"])
        ## We know we can expand ans by 2. Keep in mind,
        ## we can only do this once because only one pair of same letter words
        ## can be used as the middle of the pallindromic string.
        if any(self._map[i][i] for i in range(26)):
            ans += 2
        
        return ans
