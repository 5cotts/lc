# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if not prices:
            return max_profit
        
        min_price = prices[0]
        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
