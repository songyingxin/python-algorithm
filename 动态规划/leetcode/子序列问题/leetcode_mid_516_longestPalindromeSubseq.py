class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # dp[i][j] = dp[i+1][j-1] + 2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1])

        n = len(s) + 1
        dp = [
            [0] * n for i in range(n)
        ]
        res = 0
        for j in range(1, n):
            for i in range(1, j+1)[::-1]:
                if j == i:
                    dp[i][j] = 1
                elif j-i == 1 and s[i-1] == s[j-1]:
                    dp[i][j] = 2
                else:
                    if s[i-1] == s[j-1]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])

                res = max(res, dp[i][j])
        
        return res