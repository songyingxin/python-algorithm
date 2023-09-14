

class Solution:
    def rob(self, nums: List[int]) -> int:


        def sub_rob(sub_nums):
            n = len(sub_nums) + 1
            dp = [0] * n
            dp[1] = sub_nums[0]

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + sub_nums[i-1])
            
            return dp[-1]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        
        else:
            left = sub_rob(nums[:-1])
            right = sub_rob(nums[1:])
            
            return max(left, right)

