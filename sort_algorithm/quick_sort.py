# -*- coding: utf-8 -*-

import random

def quicksort(arr):
    """ 非原地算法 """
    if len(arr) < 2:
        return arr
    else:
        # """ 非原地算法 """
        # pivot = arr[0]
        # less = [i for i in arr[1:] if i <= pivot]
        # greater = [i for i in arr[1:] if i > pivot]

        # return quicksort(less) + [pivot] + quicksort(greater)

        """ 原地算法 """
        return quick_sort(arr, 0, len(arr) - 1)

def quick_sort(arr, low, high):
    """ 随机快排 """
    if low < high:
        index = random.randint(low, high)  # 随机快排
        arr[index], arr[high] = arr[high], arr[index]
        left, right = partition(arr, low, high)
        quick_sort(arr, low, left-1)
        quick_sort(arr, right+1, high)
    return arr


def partition(arr, low, high):
    """ 
    划分数组, 以arr[high]为分界线，将小于arr[high]的元素放到arr左边，大于arr[high] 的元素放到arr右边 
    Returns:
        left: arr[low] - arr[left-1] 存放比 arr[high] 小的元素
        right: arr[right+1] - arr[high] 存放比 arr[high] 大的元素
    """

    left = low
    right = high

    current = low
    num = arr[high]
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

    return left, right
            


if __name__== "__main__":
    print(quicksort([10, 4, 6, 7, 96, 8,23]))
