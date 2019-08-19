class Solution:
    def countSubstrings(self, s: str) -> int:

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        result = 0
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 if s[i] == s[j] and (
                        j-i <= 1 or dp[i+1][j-1] == 1) else 0

                result += dp[i][j]

        return result



