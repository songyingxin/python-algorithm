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
