# -*- coding:utf-8 -*-
import util

def insert_sort(arr):
    """ 插入排序算法实现 """
    
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
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

        if insert_sort(arr1) != sorted(arr2):
            print("the false sample is {}".format(tmp))
            print("the result of the false is {}".format(arr1))
            break
