class Solution:
    def canJump(self, nums):

        max_jump = nums[0]
        for current in range(1, len(nums)):
            if current > max_jump:
                return False
            
            max_jump = max(max_jump, current + nums[current])
        
        return True
    
nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))


