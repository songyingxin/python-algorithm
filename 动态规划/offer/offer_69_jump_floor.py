# -*- coding:utf-8 -*-

# 动态方程：f(n) = f(n-1) + f(n-2)
class Solution:
    def jumpFloor(self, number):
        # write code here

        if number < 3:
            return number

        start_one = 1
        start_two = 2
        for i in range(3, number+1):
            start_one, start_two = start_two, start_one+ start_two
        
        return start_two
