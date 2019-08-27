class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if not wordDict:
            return not s
        
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i)[::-1]:
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]

