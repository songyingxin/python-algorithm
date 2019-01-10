# -*- coding:utf-8 -*-
"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""

"""
duplication[0]: 存储重复的数字
返回值： 有重复数字：True， 无重复数字：False
"""

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        new_list = numbers[:]
        is_flag = False
        list_len = len(numbers)
        for i in numbers:
            if new_list[i] == list_len:
                duplication[0] = i
                is_flag = True
                break
            else:
                new_list[i] = list_len

        return is_flag
