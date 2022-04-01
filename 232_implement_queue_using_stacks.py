# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self._stack = []
    
    
    def empty(self) -> bool:
        return not self._stack
        

    def push(self, x: int) -> None:
        self._stack.insert(0, x)
        

    def pop(self) -> int:
        if not self.empty():
            return self._stack.pop()
        

    def peek(self) -> int:
        if not self.empty():
            return self._stack[-1]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
