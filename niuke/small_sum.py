# -*- coding:utf-8 -*-


class SmallSum:
    def merge(self, arr1, arr2):
        """ 合并两个有序数组 """
        left = 0
        right = 0

        arr1_len = len(arr1)
        arr2_len = len(arr2)

        result = 0

        while left < arr1_len and right < arr2_len:

            if arr1[left] <= arr2[right]:
                result += (arr2_len - right) * arr[left]
                left += 1
            else:
                right += 1

        return result

    def merge_sort(self, arr):
        """ 非原地算法递归实现 """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return left + right + self.merge(left, right)

    def 