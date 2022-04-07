# https://leetcode.com/problems/multiply-strings/
#
# The unicode value for "0" is 48
# The unicode value for "1" is 49
# The unicode value for "2" is 50
# The unicode value for "3" is 51
# The unicode value for "4" is 52
# The unicode value for "5" is 53
# The unicode value for "6" is 54
# The unicode value for "7" is 55
# The unicode value for "8" is 56
# The unicode value for "9" is 57
#
# See the pattern...
# 49 - 48 = 1
# 50 - 48 = 2
# 51 - 48 = 3
# ...
#
# `ord()` returns the Unicode integer of a given string.

class Solution:
    
    def _get_0_9_int_from_str(self, num: str) -> int:
        """Uses unicode conversion to get the `int` of the input `str` digit."""
        if len(num) > 1:
            raise AssertionError("I can only work with str digits 0-9!")
        return ord(num) - ord("0")
    
    def _derive_int_from_str(self, num: str) -> int:
        """Breaks a string integer (e.g., '123') into string bits.
        Converts each string bit to an integer.
        Returns an integer (e.g., 123)."""
        ans = 0
        for digit in num:
            ans = (ans * 10) + self._get_0_9_int_from_str(digit)
        return ans
    
    def multiply(self, num1: str, num2: str) -> str:
        answer = self._derive_int_from_str(num1) * self._derive_int_from_str(num2)
        return str(answer)
