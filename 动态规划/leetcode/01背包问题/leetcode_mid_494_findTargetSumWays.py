class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        total = sum(nums)
        if total < target:
            return 0
        
        diff = total - target
        if  diff % 2  != 0:
            return 0
        
        n = diff//2

        # dp[i] 装满容量为i的背包的话，有多少种方法
        dp = [0] * (n+1)
        dp[0] = 1

        for num in nums:
            for j in range(n, num-1,-1):
                dp[j] += dp[j-num]
        
        return dp[n]



