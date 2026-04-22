

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) + 1
        dp = [1] * n

        for i in range(2, n):
            for j in range(1,i):
                if nums[i-1] > nums[j-1]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)