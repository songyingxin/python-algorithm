
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        next_end = 0
        for i,num in enumerate(nums):
            if i > next_end:
                return False
            
            next_end = max(next_end, i+num)

        
        return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        next_end = 0
        for i,num in enumerate(nums):
            if i > next_end:
                return False
            
            next_end = max(next_end, i+num)
            
            if next_end > len(nums)-1:
                return True
        
        return True