# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here

        start_one = 0
        start_two = 1

        for i in range(n):
              start_one, start_two = start_two, start_one + start_two

        return start_one
