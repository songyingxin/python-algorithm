

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 以 nums[i-1] 结尾的最大递增子序列
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)