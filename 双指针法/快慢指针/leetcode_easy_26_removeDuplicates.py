

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pre = nums[0]
        left = 1

        for i,num in enumerate(nums):
            if num != pre:
                pre = num
                nums[left] = num
                left += 1
        
        return left



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

