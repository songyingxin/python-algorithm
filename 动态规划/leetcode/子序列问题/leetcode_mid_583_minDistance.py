class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # dp[i][j] = dp[i-1][j-1] else min(dp[i-1][j], do[i][j-1]) + 1       
        m = len(word1) + 1
        n = len(word2) + 1

        dp = [
            [0] * n for i in range(m)
        ]
        for i in range(1, m):
            dp[i][0] = i 
        
        for i in range(1, n):
            dp[0][i] = i

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

        return dp[-1][-1]