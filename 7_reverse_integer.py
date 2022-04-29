# https://leetcode.com/problems/reverse-integer/


MAX_INT = pow(2, 31) - 1
MIN_INT = pow(-2, 31)


class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        result = 0
        
        if is_negative:
            # Turns it positive.
            x = -x
        
        while x:
            tail = x % 10
            result = result * 10 + tail
            x //= 10
            
            # Indicates overflow error. The value is outside range(MIN_INT, MAX_INT).
            if result > MAX_INT:
                return 0
                    
        if is_negative:
            # Converts it back to negative.
            result *= -1
        
        return result
