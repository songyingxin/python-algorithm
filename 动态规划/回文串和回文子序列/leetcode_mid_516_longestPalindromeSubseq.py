class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        dp = [
            [0] * n for _ in range(n)
        ]

        for i in range(n):
            dp[i][i] = 1
        
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                if s[i] == s[j]:
                    if j-i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j-1], dp[i][j-1],dp[i+1][j])

        
        return dp[0][-1]