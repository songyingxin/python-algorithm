# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here

        help_set = set()

        for val in numbers:
            if val in help_set:
                duplication[0] = val
                return True
            help_set.add(val)
        
        return False
            

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        """ 最佳方法 """
        i = 0
        while i < len(numbers):

            if numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                tmp = numbers[i]
                numbers[i], numbers[tmp] = numbers[tmp], numbers[i]
            else:
                i += 1
        return False
