class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0
        
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]  # 第i天持有股票的最大利润
        dp[0][1] = 0           # 第i天不持有股票，且处于冷冻期的最大利润
        dp[0][2] = 0           # 第i天不持有股票，不处于冷冻期的最大利润

        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])


        return max(dp[-1])