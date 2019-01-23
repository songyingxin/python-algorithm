# -*- coding:utf-8 -*-


def bubble_end(arr):
    """ 冒泡排序实现, 从后往前冒泡 """

    for i in range(len(arr))[::-1]:
        for j in range(i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def bubble_home(arr):
    """ 冒泡排序, 从前往后冒泡 """

    for i in range(len(arr)):
        for j in range(i)[::-1]:
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


if __name__ == "__main__":
    arr = [2,5,1,6,7]
    #print(bubble_end(arr))
    print(bubble_home(arr))
    
