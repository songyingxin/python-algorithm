# -*- coding:utf-8 -*-

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        row = 0  # 行数
        column = len(array[0]) - 1  # 列数

        while row < len(array) and column >= 0:
            if array[row][column] == target:
                return True
            elif array[row][column] < target:
                row += 1
            else:
                column -= 1

        return False
