# https://leetcode.com/problems/min-cost-climbing-stairs/submissions/

from typing import List

# Use memoization to store previous calculations.
# You can use memoization to store the results of having climbed every possible path.
# Once you have the final two paths, since you are trying to optimize for costs savings,
# simply take the path that cost the least to walk.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Init the initial costs.
        idx_to_cost = {0: cost[0], 1: cost[1]}
        
        for i in range(2, len(cost)):
            # Optimizing for lowest costs means that for every step past idx 2,
            # we would have chosen the past that costs the least,
            # plus the cost of the current path.
            idx_to_cost[i] = (
                min(idx_to_cost[i - 1], idx_to_cost[i - 2]) + cost[i]
            )
        
        return min(
            # The last value in cost.
            idx_to_cost[len(cost) - 1],
            # The second to last value in cost.
            idx_to_cost[len(cost) - 2]
        )
