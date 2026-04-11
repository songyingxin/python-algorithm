

# 双指针法
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_start = 0
        t_start = 0

        while s_start < len(s) and t_start < len(t):
            if s[s_start] == t[t_start]:
                s_start += 1
                t_start += 1
            else:
                t_start += 1
        
        if s_start == len(s):
            return True
        return False


# dp[i][j]: 长度为i，末尾项为s[i-1]的子字符串，与长度为j，末尾项为t[j-1]的子字符串，二者的相同子序列长度
# if s[i-1] != t[j-1], dp[i][j] = dp[i][j-1]
# if s[i-1] == t[j-1], dp[i][j] = dp[i-1][j-1] + 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_len = len(s)
        t_len = len(t)
        dp = [[0] * (t_len+1) for _ in range(s_len+1)]

        for i in range(1, s_len+1):
            for j in range(1, t_len+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]


        return dp[-1][-1] == len(s)