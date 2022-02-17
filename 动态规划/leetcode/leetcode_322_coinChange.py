class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1 for _ in range(amount+1)]

        dp[0] = 0

        for i in range(1, amount+1):
            for val in coins:
                if val <= i:
                    dp[i] = min(dp[i], dp[i-val] + 1)

        return -1 if dp[amount] > amount else dp[amount]
    
