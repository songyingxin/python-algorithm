class Solution:
    def divisorGame(self, N: int) -> bool:
        if  N <= 0:
            return False
        dp = [False for _ in range(N+1)]
        dp[1] = False

        for i in range(1, N+1):
            for j in range(1, i):
                if i % j == 0 and dp[i-j] == False:
                    dp[i] = True
        
        return dp[-1]
