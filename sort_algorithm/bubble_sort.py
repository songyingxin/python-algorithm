# -*- coding:utf-8 -*-


def bubble_sort(arr):
    """ 冒泡排序实现 """

    for i in range(len(arr)):
        for j in range(i)[::-1]:
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr
    

if __name__ == "__main__":
    arr = [2,5,1,6,7]
    bubble_sort(arr)
    print(arr)