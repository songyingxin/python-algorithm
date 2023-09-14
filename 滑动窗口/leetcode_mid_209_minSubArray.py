class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1

        left = 0
        right = 0

        sum_val = nums[0]
        while right < len(nums):
            if sum_val >= target:
                res = min(res, right-left+1)
                sum_val -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    sum_val += nums[right]
        
        return 0 if res == len(nums)+1 else res