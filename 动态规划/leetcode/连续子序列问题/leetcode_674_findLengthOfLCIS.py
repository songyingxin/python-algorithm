

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        max_len = 1
        pre_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                pre_len += 1
            else:
                pre_len = 1

            max_len = max(pre_len, max_len)
        
        return max_len