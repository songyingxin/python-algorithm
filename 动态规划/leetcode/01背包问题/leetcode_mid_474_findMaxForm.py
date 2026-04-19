class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # dp[ii[j]:  个0，j个1 最多有 dp[i][j] 个物品
        dp = [
            [0] * (n+1) for _ in range(m+1)
        ]
        for val in strs:
            
            count_0 = val.count('0')
            count_1 = val.count('1')

            for i in range(m, count_0-1, -1):
                for j in range(n, count_1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-count_0][j-count_1]+1)

        return dp[-1][-1]