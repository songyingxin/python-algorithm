# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = deque()
        x = len(array)
        for i in range(x):
            if array[x-i-1] % 2 != 0:
                odd.appendleft(array[x-i-1])
            if array[i] % 2 == 0:
                odd.append(array[i])
        return list(odd)
