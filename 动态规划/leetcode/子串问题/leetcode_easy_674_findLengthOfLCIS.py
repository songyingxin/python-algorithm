

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # dp[i] = 1 if nums[i] < nums[i-1] else dp[i-1]+1
        dp = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + 1
            
            res = max(res, dp[i])
        
        return res

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