


# dp[n] = min(dp(n-1) + cost[n-1], dp[n-2] + cost[n-2])
# dp[0] = cost[0]
# dp[1] = cost[1]
# dp[2] = min(dp[0] + cost[0], dp[1] + cost[1])



from cmath import cos


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[n]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        if n < 2:
            return 0
        pre = 0
        pre_pre = 0
        for i in range(2, n+1):
            now = min(pre + cost[i-1], pre_pre + cost[i-2])
            pre, pre_pre = now, pre
        
        return pre
        