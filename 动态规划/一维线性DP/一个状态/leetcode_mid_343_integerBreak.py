



class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)

        for i in range(2, n+1):
            for j in range(i):
                dp[i] =  max(dp[i-j] * j, dp[i], j * (i-j))
        
        return dp[-1]
