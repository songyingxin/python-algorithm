class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        n = target + 1
        dp = [0] * n

        dp[0] = 1

        for i in range(1, n):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        
        return dp[-1]