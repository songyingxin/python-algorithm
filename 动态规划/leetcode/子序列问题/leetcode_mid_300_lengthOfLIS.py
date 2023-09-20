class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1] * len(nums)
        res = 0

        for i in range(n):
            for j in range(i)[::-1]:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
            res = max(dp[i], res)
        return res