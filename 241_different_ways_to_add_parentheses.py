# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    
    def __init__(self) -> None:
        """init varz"""
        self._operators = "-*+"
        self._memo = dict()
    
    def calc(self, num1: int, num2: int, expr: str) -> int:
        if expr == "-":
            return num1 - num2
        elif expr == "+":
            return num1 + num2
        elif expr == "*":
            return num1 * num2
        else:
            raise AssertionError("Unrecognized expression!")
            
    def diffWaysToCompute(self, expression: str) -> List[int]:     
        if expression.isdigit():
            return [int(expression)]
        elif expression in self._memo:
            return self._memo[expression]
        
        res = []
        for i in range(len(expression)):
            if expression[i] in self._operators:
                expr = expression[i]
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                res.extend(self.calc(l, r, expr) for l in left for r in right)
        
        self._memo[expression] = res
        return res
