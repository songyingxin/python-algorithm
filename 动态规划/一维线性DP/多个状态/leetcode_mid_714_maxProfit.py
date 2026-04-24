

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[i][0]: 第i天持有股票时的所得现金
        # dp[i][1]: 第i天不持有股票时的所得现金
        dp = [
            [0,0] for _ in range(n)
        ]
        # 初始化，加入第0天持有股票
        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)

        return max(dp[-1])