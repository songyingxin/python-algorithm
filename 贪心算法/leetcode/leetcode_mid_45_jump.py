class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        cur_end = 0
        res = 0
        next_end = 0

        for i in range(len(nums)):
            next_end = max(nums[i]+i, next_end)
            if i == cur_end:
                res += 1
                cur_end = next_end
                if next_end >= len(nums)-1:
                    break
        
        return res
