class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s) + 1
        dp = [
            [False] * n for i in range(n)
        ]

        max_len = 0
        res = ''
        for j in range(1, n):
            for i in range(1, j+1)[::-1]:
                if i == j:
                    dp[i][j] = True
                elif j-i==1 and s[i-1] == s[j-1]:
                    dp[i][j] = True
                else:
                    if s[i-1] == s[j-1] and dp[i+1][j-1]:
                        dp[i][j] = True

                if dp[i][j]:
                    if j-i+1 > max_len:
                        res = s[i-1:j]
                        max_len = j-i+1
        return res