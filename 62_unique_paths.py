# https://leetcode.com/problems/unique-paths

class Solution:
            
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        dp = list([0] * cols for _ in range(rows))
        
        for col in range(cols):
            dp[0][col] = 1
        
        for row in range(rows):
            dp[row][0] = 1
                        
        for row in range(1, rows):
            for col in range(1, cols):
                above_shift_val = dp[row - 1][col] 
                left_shift_val = dp[row][col - 1]
                dp[row][col] = above_shift_val + left_shift_val
                
        return dp[rows - 1][cols - 1]
