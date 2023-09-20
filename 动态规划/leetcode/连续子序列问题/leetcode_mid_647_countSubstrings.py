class Solution:
    def countSubstrings(self, s: str) -> int:

        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

        n = len(s)+1
        dp = [
            [False] * n for i in range(n)
        ]

        res = 0
        for j in range(1, n):
            for i in range(1, j+1)[::-1]:
                if i == j:
                    dp[i][j] = True
                elif j-i== 1 and s[i-1]==s[j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i-1] == s[j-1]
                
                if dp[i][j]:
                    res += 1
        
        return res