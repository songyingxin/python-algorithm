class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [
            [0] * (n+1) for _ in range(m+1)
        ]
        for val in strs:
            
            count_0 = val.count('0')
            count_1 = val.count('1')

            for i in range(count_0, m+1)[::-1]:
                for j in range(count_1, n+1)[::-1]:
                    dp[i][j] = max(dp[i][j], dp[i-count_0][j-count_1]+1)

        return dp[m][n]