# -*- coding:utf-8 -*-

def netherlands_flag(arr, low, high, num):
    """ 对数组的一段进行分界
    Args:
        low: 要分界的数组的下界
        high： 要分界的数组的上界
    """

    left = low   # left = 0
    right = high  # right = len(arr) - 1

    current = low  # current = 0

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

if __name__ == "__main__":
    arr = [10, 4, 6, 7, 96, 8, 23]
    netherlands_flag(arr, 0,len(arr)-1,23)
    print(arr)
