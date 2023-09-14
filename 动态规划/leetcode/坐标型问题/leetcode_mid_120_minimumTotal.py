# 二维空间
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        dp = [
            [0] * n for i in range(n)
        ]

        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] =min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        return min(dp[-1]) 





# 一维空间优化
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        mini, M = triangle[-1], len(triangle)
        for i in range(M-2, -1, -1):
            for j in range(len(triangle[i])):
                mini[j] = triangle[i][j] + min(mini[j], mini[j+1])
        
        return mini[0]
