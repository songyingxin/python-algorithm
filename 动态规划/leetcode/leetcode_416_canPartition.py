class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        num_sum = sum(nums)

        # 如果和不是偶数，则必然无法平分
        if num_sum % 2 != 0:
            return False

        target = num_sum // 2
        dp = [
            [False for _ in range(target+1)] 
                    for _ in range(len(nums)) 
        ]

        for i in range(target + 1):
            dp[0][i] = False if nums[0] != i else True
        
        for i in range(1, len(nums)):
            for j in range(target + 1):
                dp[i][j] = dp[i-1][j] or (nums[i] <= j and dp[i-1][j-nums[i]])
        
        return dp[-1][-1]





