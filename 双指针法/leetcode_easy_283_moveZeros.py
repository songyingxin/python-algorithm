# -*- coding:utf-8 -*-

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

