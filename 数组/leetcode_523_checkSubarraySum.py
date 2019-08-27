class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:







# 扩展1
def get_max_len(nums, target):

    left = 0
    right = 0
    sum_val = nums[0]
    max_len = 0

    while right < len(nums):
        if sum_val == target:
            max_len = max(max_len, right - left + 1)
            sum_val += nums[left]
            left += 1
        elif sum_val < target:
            right += 1
            # 保证 right 不越界
            if right == len(nums):
                break
            sum_val += nums[right]
        else:
            sum_val += nums[left]
            left += 1