class Solution:
    def canJump(self, nums: List[int]) -> bool:

        next_end = 0

        for i in range(len(nums)):
            if i > next_end:
                return False
            
            next_end = max(next_end, i+nums[i])

            # 剪枝操作
            if next_end > len(nums) - 1:
                return True
        
        return True