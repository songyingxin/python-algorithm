# 二维空间
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        
        dp = [[0] * len(triangle[-1]) for i in range(n)]
        for i in range(len(triangle[-1])):
            dp[-1][i] = triangle[-1][i]

        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]




# 一维空间优化
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        mini, M = triangle[-1], len(triangle)
        for i in range(M-2, -1, -1):
            for j in range(len(triangle[i])):
                mini[j] = triangle[i][j] + min(mini[j], mini[j+1])
        
        return mini[0]
