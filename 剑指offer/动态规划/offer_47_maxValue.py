

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:

        # dp[0][0] = grid[0][0]
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        
        for j in range(1,n):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = max(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        
        return grid[-1][-1]
