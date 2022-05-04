# https://leetcode.com/problems/longest-palindrome/

from collections import Counter

class Solution:
        
    def longestPalindrome(self, s: str) -> int:
        """I count how many letters appear an odd number of times.
        Because we can use all letters, except for each odd-count
        letter we must leave one, except one of them we can use."""
        count = Counter(s)
        odds = sum(v % 2 != 0 for v in count.values())
        return len(s) - odds + int(bool(odds))
