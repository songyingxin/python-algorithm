class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True
        for index, num in enumerate(nums):
            for j in range(num, target+1)[::-1]:
                dp[j] |= dp[j-num]
        
        return dp[target]
