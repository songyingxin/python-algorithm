class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        start = nums[0]
        for val in nums[1:]:
            start ^= val
        
        return start
