# -*- coding:utf-8 -*-

""" 对希尔排序的实现 """

def shell_sort(arr):

    N = len(arr)
    h = 1

    while h < N/3 :
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, N):

            for j = i
