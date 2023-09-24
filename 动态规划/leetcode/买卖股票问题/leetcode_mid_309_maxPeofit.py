class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        sell = [0 for _ in range(n)]
        buy = [0 for _ in range(n)]
        cooldown = [0 for _ in range(n)]

        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            buy[i] = max(buy[i-1], cooldown[i-1]-prices[i])
            cooldown[i] = max(cooldown[i-1], max(sell[i-1], buy[i-1]))
        
        return sell[-1]



