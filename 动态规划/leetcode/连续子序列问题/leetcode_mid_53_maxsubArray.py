



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        
        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        pre= nums[0]
        max_val = nums[0]

        for i in range(1, len(nums)):
            pre = max(pre + nums[i], nums[i])
            max_val = max(pre, max_val)
        return max_val
