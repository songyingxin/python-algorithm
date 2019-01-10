# -*- coding:utf-8 -*-

""" 插入排序算法实现 """


def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

if __name__ == "__main__":

    print(insert_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
