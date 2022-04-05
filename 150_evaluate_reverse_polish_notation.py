# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    
    def __init__(self) -> None:
        """init varz"""
        self._operations_maps = {
            '+': (lambda a, b: a+b),
            '-': (lambda a, b: b-a),
            '*': (lambda a, b: b*a),
            # `int()` truncates towards zero
            # single `/` for floating point division
            '/': (lambda a, b: int(b/a)),
        } 
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self._operations_maps:
                stack.append(
                    self._operations_maps[token](stack.pop(), stack.pop())
                )
            else:
                # Need to coerce token to int because it is str.
                stack.append(int(token))
        
        # The only remaining item in the stack
        # should be the result of all the above operations.
        return stack[0]
