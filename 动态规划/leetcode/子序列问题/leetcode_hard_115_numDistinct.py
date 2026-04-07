


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s) + 1
        n = len(t) + 1

        dp = [[0] * (n) for i in range(m)]

        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]