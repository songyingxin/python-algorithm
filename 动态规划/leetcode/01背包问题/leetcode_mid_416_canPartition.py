
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if len(nums) < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        n = total // 2 
        dp = [0] * (n+1)

        for num in nums:
            for i in range(n, num-1, -1):
                dp[i] = max(dp[i], dp[i-num] + num)
        
        return dp[-1] == n








