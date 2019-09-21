class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])
        dp = [[0 for i in range(N)]
                    for j in range(M)]
        dp[0][0] = grid[0][0]
        for i in range(1, M):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for i in range(1, N):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]

