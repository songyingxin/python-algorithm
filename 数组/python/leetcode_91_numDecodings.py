class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        pre = 1   # dp[i-2]
        curr = 1  # dp[i-1]

        for i in range(1, len(s)):
            tmp = curr
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    curr = pre
                else:
                    return 0
            
            elif s[i-1] == '1' or (s[i-1] == '2' and s[i] >= '1' and s[i] <= '6'):
                curr += pre
            
            pre = tmp
        
        return curr


