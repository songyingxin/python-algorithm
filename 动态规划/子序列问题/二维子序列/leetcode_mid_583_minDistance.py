


# 先找到最长公共子序列，然后进行运算最短路径
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1) + 1
        n = len(word2) + 1

        # word1[:i], word[:j] 的最长子序列
        dp = [
            [0] * n for _ in range(m)
        ]

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return len(word1) - dp[-1][-1] * 2 + len(word2)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
     
        m = len(word1) + 1
        n = len(word2) + 1

        # word1[:i], word2[:j] 所需的最小步数
        dp = [
            [0] * n for i in range(m)
        ]
        for i in range(1, m):
            dp[i][0] = i 
        
        for i in range(1, n):
            dp[0][i] = i

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

        return dp[-1][-1]