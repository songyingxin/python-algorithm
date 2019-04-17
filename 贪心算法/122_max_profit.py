class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        vals = [prices[i] - prices[i-1] for i in range(1, len(prices))]

        result = 0

        for val in vals:
            if val > 0:
                result += val

        return result
