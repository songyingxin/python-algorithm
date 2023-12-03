class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        sum_val = sum(nums)
        diff = sum_val - target
        if  diff < 0 or diff % 2  != 0:
            return 0
        
        neg = diff//2
        dp = [0] * (neg+1)
        dp[0] = 1

        for num in nums:
            for j in range(num, neg+1)[::-1]:
                dp[j] += dp[j-num]
        
        return dp[neg]