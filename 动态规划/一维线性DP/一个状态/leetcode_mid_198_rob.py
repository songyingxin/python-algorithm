

class Solution:
    def rob(self, nums: List[int]) -> int:

        # dp[i]: 第i个房间偷到的最大金额
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        n = len(nums) + 1
        dp = [0] * n 

        dp[1] = nums[0]

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        

        return dp[-1]



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums) 
        
        one = nums[0]
        two = max(nums[:2])

        for num in nums[2:]:
            one, two = two, max(one+num, two)


        return two
        
