class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return len(nums)
        
        pre_diff = 0
        res = 1
        for i in range(len(nums)-1):
            cur_diff = nums[i+1] - nums[i]
            if (pre_diff <= 0 and cur_diff > 0) or (pre_diff >= 0 and cur_diff < 0):
                res += 1
                pre_diff = cur_diff
        
        return res