
# 常规解法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 1
        pre = nums[0]  # 前一个出现的数
        times = 1  # 出现次数
        for i in range(1, len(nums)):
            if nums[i] != pre:
                nums[left] = nums[i]
                left += 1
                pre = nums[i]
                times = 1
            else:
                if times == 1:
                    nums[left] = nums[i]
                    left += 1
                    times += 1

        return left


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 0
        
        for i in range(len(nums)):
            if left > 1 and nums[i] == nums[left-1] == nums[left-2]:
                continue
            
            nums[left] = nums[i]
            left += 1
        
        return left

