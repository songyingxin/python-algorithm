# 先遍历背包，再遍历物品
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [float('inf')] * n

        # dp[i]：凑成金额为i时所需的最小硬币数
        dp[0] = 0

        for i in range(1, n):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]



# 先遍历物品，再遍历背包
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1

        # dp[i]：凑成金额为i时所需的最小硬币数
        dp = [float('inf')] * n
        dp[0] = 0

        for coin in coins:
            for i in range(1, n):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]


