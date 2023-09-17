class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            res += max(0, profit)
        
        return res