# https://leetcode.com/problems/coin-change/

from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Maintain answers for amounts 0 to `amount`. The index is the `amount`.
        dp = [inf for _ in range(amount + 1)]
        # This is the base case. When amount == 0, the coins needed are also zero.
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    # If the coin is less than the target amount,
                    # we know we have a new potential solution for
                    # the fewst number of coints needed to equal i.
                    # It would be this coin, plus whatever other coints
                    # we have already computed at that target amount.
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return -1 if dp[-1] == inf else dp[-1]
