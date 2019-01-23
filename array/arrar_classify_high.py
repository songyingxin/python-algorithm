# -*- coding:utf-8 -*-
def classify_arr(arr, num):
    """ 荷兰国旗问题 """
    left = -1
    right = len(arr)

    current = 0

    while current < right:
        if arr[current] < num:
            arr[left+1], arr[current] = arr[current], arr[left+1]
            left += 1
            current += 1
        elif arr[current] > num:
            arr[right-1], arr[current] = arr[current], arr[right-1]
            right -= 1
        else:
            current += 1

def classify_arr_high(arr, low, high, num):
    """ 荷兰国旗问题，复杂实现 
    Args:
        low: 要classify的下界
        high： 要classify 的上界
    """

    left = low - 1
    right = high + 1

    current = low 

    while current < right:
        if arr[current] < num:
            arr[left+1], arr[current] = arr[current], arr[left+1]
            left += 1
            current += 1
        elif arr[current] > num:
            arr[right-1], arr[current] = arr[current], arr[right-1]
            right -= 1
        else:
            current += 1

if __name__ == "__main__":
    arr = [45, 2, 5, 78, 2, 87, 5, 4, 7, 23, 45, 56, 89]
    classify_arr_high(arr, 0, len(arr)-1, 5)
    print(arr)
