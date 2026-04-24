


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1) + 1
        n = len(text2) + 1

        dp = [
            [0] * n for i in range(m)
        ]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[-1][-1]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # dp[i][j] 以下标i,j结尾的最长公共子序列的长度
        dp = [
            [0] * n for _ in range(m)
        ] 

        # 初始化，此处是关键
        for i in range(m):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            elif i > 0:
                dp[i][0] = dp[i-1][0]
        
        for i in range(n):
            if text1[0] == text2[i]:
                dp[0][i] = 1
            elif i > 0:
                dp[0][i] = dp[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] =  dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]


