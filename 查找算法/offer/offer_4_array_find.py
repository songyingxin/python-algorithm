# -*- coding:utf-8 -*-

# https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=23256&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

# 分析：如果数组中的数字小于要查找的数字，则要查找的数字应该在当前数字位置的右边或下边； 如果选取的数字大于要查找的数字，那么要查找的数字应该在当前数字位置的上边或左边。
# 思路：首先选取数组中右上角（从左下角也可）数字。 如果该数字等于要查找的数字，则查找过程结束； 如果该数字大于要查找的数字，则剔除这个数字所在的列； 如果该数字小于要查找的数字，则剔除这个数字所在的行。

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        row = 0  # 行数
        col = len(array[0]) - 1  # 列数

        while row < len(array) and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                row += 1
            else:
                col -= 1

        return False
