# -*- coding:utf-8 -*-

def binary_search(items, item):
    low = 0
    high = len(items) - 1

    while low <= high:

        mid = low + (high-low) // 2
        guess = items[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    return low


def binary_search_high(arr, n, target):
    """在 arr 的 前n个元素内查找target """
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high-low) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

if __name__ == "__main__":
    example = [1, 3, 5, 6, 7, 9, 11, 17, 43, 67, 432]

    print(binary_search_high(example,10, 17 ))
