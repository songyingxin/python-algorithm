class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_val = prices[0]
        max_profit = 0

        for val in prices[1:]:
            if val < min_val:
                min_val = val
                continue
            max_profit = max(max_profit, val-min_val)

        return max_profit
