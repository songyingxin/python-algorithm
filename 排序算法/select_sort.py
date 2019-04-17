# -*- coding:utf-8 -*-

import util

def find_smallest(arr, left, right):
    smallest = arr[left]
    smallest_index = left

    for i in range(left, right + 1):
        if arr[i] < arr[smallest_index]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):

    for i in range(len(arr)):
        smallest_index = find_smallest(arr, i, len(arr)-1)
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


if __name__ == "__main__":
    test_time = 100
    max_size = 10
    max_value = 10
    min_value = 0
    for i in range(test_time):
        arr1 = util.get_random_array(max_size, min_value, max_value)
        arr2 = arr1.copy()
        selection_sort(arr1)
        if arr1 != sorted(arr2):
            print("the false sample is {}".format(arr2))
            print("the result of the false is {}".format(arr1))
            break
