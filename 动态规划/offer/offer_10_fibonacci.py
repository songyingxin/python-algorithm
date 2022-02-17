# -*- coding:utf-8 -*-

# 动态规划思路， 动态方程： f(n) = f(n-1) + f(n-2)
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        one = 1
        two = 1
        for i in range(n-2):
            one,two = two, one+two 
        return two
