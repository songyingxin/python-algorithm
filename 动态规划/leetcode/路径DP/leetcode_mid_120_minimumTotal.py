# 二维空间
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = [row.copy() for row in triangle]

        m = len(triangle)

        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
        
        for i in range(1, m):
            n = len(triangle[i])
            for j in range(1, n):
                if j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
        return min(dp[-1]) 





# 一维空间优化，自底向上
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = triangle[-1].copy()  # 用最后一行初始化
        
        for i in range(m-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        
        return dp[0]
