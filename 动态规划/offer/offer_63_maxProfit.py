

# 思路：动态规划
# dp[i][j]: 下标为i这一天结束的时候，手上持股状态为j时，我们持有的现金数
# j=0：当前不持股
# j=1： 当前持股
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        length = len(prices)
        if length < 2:
            return 0
        
        dp = [[0] * 2] * length
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        
        return dp[length-1][0]


class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        inf = int(1e9)
        min_price = inf
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit
