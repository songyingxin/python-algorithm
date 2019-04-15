# -*- coding:utf-8 -*-

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.netherlands_flag(nums, 0, len(nums) - 1, 1)
        print(nums)

    def netherlands_flag(self, arr, low, high, num):
        """ 对数组的一段进行分界
        Args:
            low: 要分界的数组的下界
            high： 要分界的数组的上界
        """

        left = low   # left = 0
        right = high  # right = len(arr) - 1

        current = low  # current = 0

        while current <= right:
            if arr[current] < num:
                arr[left], arr[current] = arr[current], arr[left]
                left += 1
                current += 1
            elif arr[current] > num:
                arr[right], arr[current] = arr[current], arr[right]
                right -= 1
            else:
                current += 1

if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(arr)
