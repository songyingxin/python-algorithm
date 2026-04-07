

class Solution:
    def countSubstrings(self, s: str) -> str:

        n = len(s) + 1
        dp = [
            [False] * n for i in range(n)
        ]

        res = 0
        for j in range(1, n):
            for i in range(1, j+1)[::-1]:
                if i == j:
                    dp[i][j] = True
                elif j-i==1 and s[i-1] == s[j-1]:
                    dp[i][j] = True
                else:
                    if s[i-1] == s[j-1] and dp[i+1][j-1]:
                        dp[i][j] = True

                if dp[i][j]:
                    res += 1
                    
        return res


class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        # [i,j] 区间内的字符串是否为回文
        dp = [
            [False] * n for _ in range(n)
        ] 

        res = 0

        # 字符串长度为1 的皆为回文
        for i in range(n):
            dp[i][i] = True
        res += n

        # 字符串长度为2的回文判断
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1

        # 递推公式
        for j in range(2, n):
            for i in range(j-2,-1,-1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]

                if dp[i][j]:
                    res += 1
        
        return res