# -*- coding:utf-8 -*-

# 动态规划方程: f(1) = 1, f(2) = 2, f(n) = f(n-1) + f(n-2)
class Solution:
    def rectCover(self , number: int) -> int:
        # write code here
        if number == 0:
            return 0
        
        start_one = 1
        start_two = 2

        for i in range(number-1):
              start_one, start_two = start_two, start_one + start_two

        return start_one
