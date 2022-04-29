# # https://leetcode.com/problems/sum-of-two-integers/
# # Lots of inspiration from:
# # https://stackoverflow.com/questions/38557464/sum-of-two-integers-without-using-operator-in-python

# import sys

# # If the variable has a signed integer type, a program may make the
# # assumption that a variable always contains a positive value. An integer
# # overflow can cause the value to wrap and become negative, which violates
# # the program's assumption and may lead to unexpected behavior (for example,
# # 8-bit integer addition of 127 + 1 results in −128, a two's complement of 128).
# # (A solution for this particular problem is to use unsigned integer types for
# # values that a program expects and assumes will never be negative.)
# # 
# # There are 127 possible bytes for a a positive 32 bit int.
# #
# # https://en.wikipedia.org/wiki/Integer_overflow

# MAX_INT = 0x7FFFFFFF
# MIN_INT = 0x80000000
# MASK = 0x100000000


# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         while b:
#             # "^" does the summation.
#             a = (a ^ b) & MASK
            
#             # (a & b) << 1 represents the carry left over from the above summation.
#             #
#             # First iteration (a is 20, b is 20)
#             # 10100 ^ 10100 == 00000 # makes a 0
#             # (10100 & 10100) << 1 == 101000 # makes b 40
#             #
#             # Second iteration:
#             # 000000 ^ 101000 == 101000 # Makes a 40
#             # (000000 & 101000) << 1 == 0000000 # Makes b 0
#             b = ((a & b) << 1) & MASK
        
#         # All the masks are doing is ensuring that the value is an integer,
#         # because your code even has comments stating that a, b, and the
#         # return type are of type int.
#         if a <= MAX_INT:
#             return a
#         else:
#             return ~(a ^ MASK)

class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
