# https://leetcode.com/problems/detect-squares/

# https://leetcode.com/problems/detect-squares/submissions/
    
from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self._coords = defaultdict(int)
        
        
    def add(self, point: List[int]) -> None:
        self._coords[tuple(point)] += 1
            

    def count(self, point: List[int]) -> int:
        input_x, input_y = point
        num_squares = 0
        for x, y in set(self._coords.keys()):
            # We don't want to compare the same values.
            if input_x == x and input_y == y:
                continue
            # If the distance between the input X and X and input Y and Y are the same,
            # we know we can form a square with any coordinates that use these Xs and Ys.
            # We use `abs()` because we just care about the distance.
            # For example, the distance between 2 and 10 is 8,
            # whether we do 2- 10 = -8 or 10 - 2 = 8.
            elif abs(x - input_x) == abs(y - input_y):
                # Recall, `defaultdict(int)[x]` will return Zero if X is not in the keys (it also adds x to the keys).
                # Therefore, if any of the coordinates do not have a point at them, the whole val is zero.
                # If any of the coordinates have more than one point at them, multiple squares are formed.
                point1 = self._coords[(x, y)]
                point2 = self._coords[(input_x, y)]
                point3 = self._coords[(x, input_y)]
                num_squares += point1 * point2 * point3
        return num_squares
                

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
