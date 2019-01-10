# -*- coding:utf-8 -*-

""" 思想： 从数组中取出最大/最小的元素放入另一数组，然后将次大/次小的元素提出，以此类推 """

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index, smallest

def selection_sort1(arr):
    """ 空间复杂度较高版本 """
    sorted_arr = []
    for i in range(len(arr)):
        smallest_index, smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr


def selection_sort2(arr):
    """ 空间复杂度低版本 """

    for i in range(len(arr)):
        smallest_index, smallest  = find_smallest(arr[i:])
        temp = arr[i]
        arr[i] = arr[i + smallest_index]
        arr[i + smallest_index] = temp

    return arr



if __name__ == "__main__":


    a = selection_sort1([3, 5,6, 7,12, 3, 69, 12, 45,65])
    print(a)


    b = selection_sort2([3, 5, 90, 45, 36, 65, 21, 43, 7, 7, 12, 45,65])
    print(b)
