class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)

        # 区间 [i,j] 的字符串的最长回文子串
        dp = [
            [0] * n for _ in range(n)
        ]

        # 长度为1的字符串皆为回文
        for i in range(n):
            dp[i][i] = 1

        # 递推公式
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return  dp[0][-1]