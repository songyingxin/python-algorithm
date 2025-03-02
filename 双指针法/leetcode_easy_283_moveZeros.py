# -*- coding:utf-8 -*-

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        for  num in nums:
            if num != 0:
                nums[left] = num
                left += 1
        
        for i in range(left, len(nums)):
            nums[i] = 0
        
        return nums

# 思路2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if left != i:   # 为了优化， 去掉也对
                    nums[left], nums[i] = nums[i], nums[left]
                left += 1

