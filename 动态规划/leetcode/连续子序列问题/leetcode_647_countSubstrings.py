


# dp[i][j]: nums[i:j] 的字符串是否为回文子串
# if nums[i] == nums[j] and dp[i-1][j-1], dp[i][j] = 1
# else: dp[i][j] = 0

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        s_len = len(s)
        dp = [[False] * s_len for _ in range(s_len)]
        
        for j in range(s_len):
            for i in range(j+1):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
        
        return res