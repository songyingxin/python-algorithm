# 易理解版本
class Solution:
    def maxSubArray(self, nums):
        dp = [0 for i in range(len(nums))]
        max_val = nums[0]
        dp[0] = nums[0]
        if dp[0] < 0:
            dp[0] = 0

        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + nums[i]
            max_val = max(max_val, dp[i])
            if dp[i] < 0:
                dp[i] = 0
        
        return max_val

# 最优化版本
class Solution:
    def maxSubArray(self, nums):
        cur = 0
        max_val = nums[0]

        for i in range(len(nums)):
            cur = cur + nums[i]
            max_val = max(max_val, cur)
            if cur < 0:
                cur = 0
        return max_val



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [1, 2, -1, -2, 2, 1, -2, 1]
print(Solution().maxSubArray(nums))
