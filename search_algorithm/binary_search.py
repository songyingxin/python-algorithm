# -*- coding:utf-8 -*-

""" 二分查找 """

def binary_search(items, item):
    low = 0
    high = len(items) - 1

    while low <= high:

        mid = (low + high) // 2
        guess = items[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    return low

if __name__ == "__main__":
    example = [1, 3, 5, 6, 7, 9]

    print(binary_search(example,0 ))
