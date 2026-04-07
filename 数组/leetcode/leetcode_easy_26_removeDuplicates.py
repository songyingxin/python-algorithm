class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        for num in nums[1:]:
            if num == nums[left]:
                continue
            else:
                left += 1
                nums[left] = num
        
        return left + 1

