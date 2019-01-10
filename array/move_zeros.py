# -*- coding:utf-8 -*-



class Solution_simple:
    """ 解法 1 的非原地算法实现，时间复杂度 O(n), 空间复杂度 O(n) """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        other_num = []
        for num in nums:
            if num != 0:
                other_num.append(num)

        for i in range(len(nums)):
            if i < len(other_num):
                nums[i] = other_num[i]
            else:
                nums[i] = 0 


class Solution_middle:
    """ 解法 1 的原地算法实现，时间复杂度 O(n), 空间复杂度 O(1) """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        for num in nums:
            if num != 0:
                nums[left] = num
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0


class Solution_high:
    """ 解法 1 的原地算法实现，时间复杂度 O(n), 空间复杂度 O(1) """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if (left != i):  # 用于减少交换的次数
                    nums[left], nums[i] = nums[i], nums[left]
                left += 1
  

if __name__ == "__main__":
    
    arr = [0, 1, 0, 3, 12]

    Solution_high().moveZeroes(arr)
    print(arr)

