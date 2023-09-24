class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s) + 1
        dp = [False] * n
        dp[0] = True

        word_dict = set(wordDict)
        for i in range(1, n):
            for j in range(i)[::-1]:
                if dp[j] and s[j:i] in word_dict:
                    dp[i] = True
                    break
        
        return dp[-1]

