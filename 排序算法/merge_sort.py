# -*- coding:utf-8 -*-
import util
class MergeSort:
    def merge(self, arr1, arr2):
        """ 合并两个有序数组 """
        left = 0
        right = 0
        result = []
        while left < len(arr1) and right < len(arr2):
            if arr1[left] <= arr2[right]:
                result.append(arr1[left])
                left += 1
            else:
                result.append(arr2[right])
                right += 1
            
        if left < len(arr1):
            result.extend(arr1[left:])
        if right < len(arr2):
            result.extend(arr2[right:])

        return result

    def merge_sort(self, arr):
        """ 归并排序算法递归实现 """
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)


class MergeSortOptimize:
    def merge_sort(self, arr):

        if len(arr) < 2:
            return
        self._merge_sort(arr, 0, len(arr) - 1)


    def merge(self, arr, start, mid, end):
        """ 合并两个有序数组 """
        help_arr = []
        left_ptr = start
        right_str = mid + 1

        while left_ptr <= mid and right_str <= end:
            if arr[left_ptr] <  arr[right_str]:
                help_arr.append(arr[left_ptr])
                left_ptr += 1
            else:
                help_arr.append(arr[right_str])
                right_str += 1
        while left_ptr <= mid:
            help_arr.append(arr[left_ptr])
            left_ptr += 1
        
        while right_str <= end:
            help_arr.append(arr[right_str])
            right_str += 1
        
        for i in range(len(help_arr)):
            arr[start + i] = help_arr[i]


    def _merge_sort(self, arr, start, end):
        """ 归并排序算法递归实现 """
        if start == end:
            return

        mid = (start + end) // 2
        self._merge_sort(arr, start, mid)
        self._merge_sort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)

if __name__ == "__main__":
    test_time = 100
    max_size = 100
    max_value = 100
    min_value = 0
    for i in range(test_time):
        arr1 = util.get_random_array(max_size, min_value, max_value)
        arr2 = arr1.copy()

        MergeSortOptimize().merge_sort(arr1)

        if   arr1 != sorted(arr2):
            print("the false sample is {}".format(tmp))
            print("the result of the false is {}".format(arr1))
            break
