# -*- coding:utf-8 -*-

import util

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):

    for i in range(len(arr)):
        smallest_index = find_smallest(arr[i:])

        arr[i], arr[i+smallest_index] = arr[i + smallest_index], arr[i]

    return arr


if __name__ == "__main__":
    test_time = 5000
    max_size = 100
    max_value = 100
    min_value = 0
    for i in range(test_time):
        arr1 = util.get_random_array(max_size, min_value, max_value)
        arr2 = arr1.copy()
        tmp = arr1.copy()
        if selection_sort(arr1) != sorted(arr2):
            print("the false sample is {}".format(tmp))
            print("the result of the false is {}".format(arr1))
            break
