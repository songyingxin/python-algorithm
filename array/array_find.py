# -*- coding:utf-8 -*-
"""
二维数组中的查找：
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

""" 方法1： 采用顺序查找"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        is_exit = False
        if array == [[]]:
            return False
        for value_list in array:
            length = len(value_list)
            min = value_list[0]
            max = value_list[length-1]
            if min <= target <= max:
                for value in value_list:
                    if value == target:
                        return True
                    else:
                        continue
            else:
                continue
        return is_exit

target = 16
array = [[]]
print(Solution().Find(target, array))



""" 方法2： 采用折半查找"""
