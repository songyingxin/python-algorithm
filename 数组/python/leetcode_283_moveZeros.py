# -*- coding:utf-8 -*-

# 思路1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1

        while left < len(nums):
            nums[left] = 0
            left += 1

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







if __name__ == "__main__":
    
    arr = [0, 1, 0, 3, 12]

    Solution_high().moveZeroes(arr)
    print(arr)

