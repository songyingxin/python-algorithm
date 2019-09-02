class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        left = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left += 1
        return left

