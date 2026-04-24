class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = amount + 1
        # dp[i]: 装满背包容量为i的背包，有多少种方法
        dp = [0] * n
        dp[0] = 1

        for coin in coins:
            for i in range(coin, n):
                dp[i] += dp[i-coin]
        
        return dp[-1]