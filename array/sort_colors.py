# -*- coding:utf-8 -*-

class Solution_simple:
    """ 解法1， 计数排序，时间复杂度为 O(n)， 空间复杂度为 O(1) """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        color_count = [0,0,0]

        for num in nums:
            assert num >=0 and num <= 2
            color_count[num] += 1

        index = 0

        for i in range(3):
            for j in range(color_count[i]):
                nums[index] = i
                index += 1


class Solution_high:
    """ 解法2， 三路排序，时间复杂度为 O(n)， 空间复杂度为 O(1) """

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = -1   # [0...zero] = 0
        two = len(nums)    # [two...n-1] = 2

        i = 0 
        while i < two:
            if nums[i] == 1:
               i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                assert nums[i] == 0
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1

if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0]
    Solution_high().sortColors(arr)
    print(arr)

