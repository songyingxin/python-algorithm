class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        
        end = 0

        for i in range(len(nums)):
            if i <= end:
                end = max(i+nums[i], end)
                if end >= len(nums)-1:
                    return True
        
        return False