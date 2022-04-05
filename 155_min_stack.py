from math import inf

class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = [inf]
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        if val <= self.getMin():
            self._min_stack.append(val)
        

    def pop(self) -> None:
        if self._stack.pop(-1) == self.getMin():
            self._min_stack.pop(-1)
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]
