class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:


        total = sum(stones)
        n = total // 2

        # 背包容量为下标i时的最大重量
        dp = [0] * (n+1)

        for weight in stones:
            for i in range(n, weight-1, -1):
                dp[i] = max(dp[i], dp[i-weight] + weight)

        return total - 2 * dp[-1]



class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:


        total = sum(stones)
        n = len(stones)
        m = total // 2

        dp = [False] * (m+1)
        dp[0] = True

        for weight in stones:
            for j in range(weight, m+1)[::-1]:
                dp[j] |= dp[j-weight]
        
        res = None
        for j in range(m+1)[::-1]:
            if dp[j]:
                res = total - 2 * j
                break
        return res
