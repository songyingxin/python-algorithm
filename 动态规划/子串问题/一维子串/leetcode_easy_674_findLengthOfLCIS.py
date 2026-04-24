

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + 1
        
        return max(dp)

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        max_len = 1
        pre_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                pre_len += 1
            else:
                pre_len = 1

            max_len = max(pre_len, max_len)
        
        return max_len