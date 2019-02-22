# -*- coding:utf-8 -*-

""" 思想： 从数组中取出最大/最小的元素放入另一数组，然后将次大/次小的元素提出，以此类推 """

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

        arr[i], arr[i + smallest_index] = arr[i + smallest_index], arr[i]

    return arr