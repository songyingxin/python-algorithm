class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = prices[0]
        max_profit = 0

        for val in prices[1:]:
            max_profit = max(max_profit, val-min_val)
            min_val = min(min_val, val)

        return max_profit
