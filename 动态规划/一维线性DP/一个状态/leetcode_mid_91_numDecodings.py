class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # 第一个字符
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, n + 1):
            # 1. 一位组合
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
            
            # 2. 两位组合
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]