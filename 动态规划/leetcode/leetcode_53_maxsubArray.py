class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        pre= nums[0]
        max_val = nums[0]

        for i in range(1, len(nums)):
            pre = max(pre + nums[i], nums[i])
            max_val = max(pre, max_val)
        return max_val
