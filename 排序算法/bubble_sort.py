# -*- coding:utf-8 -*-

import util

def bubble_end(arr):
    """ 冒泡排序实现, 从前往后冒泡， 最后的几个元素有序且最大 """

    if len(arr) < 2:
        return arr

    for end in range(len(arr))[::-1]:   # len(arr)-1, ... , 0
        for j in range(end):        # 0, ... end
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def bubble_home(arr):
    """ 冒泡排序, 从后往前冒泡，最前面的几个元素有序且最大 """
    if len(arr) < 2:
        return arr
        
    for start in range(len(arr)):   # 0, ... , len(arr)-1
        for j in range(start,len(arr)-1)[::-1]:    # len(arr)-1, ..., start 
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


if __name__ == "__main__":
    test_time = 5000
    max_size = 100
    max_value = 100
    min_value = 0
    for i in range(test_time):
        arr = util.get_random_array(max_size, min_value, max_value)
        arr1 = arr.copy()
        arr2 = arr.copy()
        tmp = arr1.copy()
        if bubble_end(arr1) != sorted(arr):
            print("the false sample is {}".format(tmp))
            break
        
        if bubble_home(arr2) != sorted(arr):
            print("the false sample is {}".format(tmp))
            break



    
