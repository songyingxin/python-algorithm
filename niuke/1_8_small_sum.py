# -*- coding:utf-8 -*-

class SmallSum:
    def small_sum(self, arr):

        if len(arr) < 2:
            return 0
        return self._merge_sort(arr, 0, len(arr) - 1)

    def merge(self, arr, start, mid, end):
        """ 合并两个有序数组 """
        result = 0

        help_arr = []
        left_ptr = start
        right_str = mid + 1

        while left_ptr <= mid and right_str <= end:
            if arr[left_ptr] < arr[right_str]:
                result += (end - right_str + 1) * arr[left_ptr]
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
        
        return result

    def _merge_sort(self, arr, start, end):
        """ 归并排序算法递归实现 """
        if start == end:
            return 0

        mid = (start + end) // 2   # start + (end - start) // 2
        return  self._merge_sort(arr, start, mid) + self._merge_sort(arr, mid + 1, end) + self.merge(arr, start, mid, end)

# 对数器， 用来验证结果是否正确
def  comparator(arr):

    if  len(arr) < 2:
        return 0
    
    result = 0
    for i in range(len(arr)):
        for j in range(i):
            result += arr[j] if arr[j] < arr[i] else 0
    
    return result

import random

def generate_samples(max_size, min_val, max_val):
    return [random.randint(min_val, max_val) for i in range(max_size)]

if __name__ == "__main__":
    times = 100

    for i in range(times):
        arr1 = generate_samples(5, -10, 10)
        arr2 = arr1.copy()
        predict = SmallSum().small_sum(arr1)
        label = comparator(arr2)

        if  predict != label:
            print("the false sample is {}".format(arr2))
            print("the result of the false is {}".format(predict))
            print("the compator's result is {}".format(label))
            break
