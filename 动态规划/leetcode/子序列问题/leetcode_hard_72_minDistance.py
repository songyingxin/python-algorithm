

# dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if a[i] != a[j]
# dp[i][j] = min(dp[i-1][j-1]-1, dp[i-1][j], dp[i][j-1]) + 1 if a[i] == a[j]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        # 有一个字符串为空串
        if n==0 or m==0:
            return n + m
        
        n += 1
        m += 1

        # DP 数组
        dp = [ [0] * (n) for _ in range(m)]
        
        # 边界状态初始化
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        
        # 计算所有 DP 值
        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[-1][-1]

