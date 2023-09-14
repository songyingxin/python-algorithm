# -*- coding:utf-8 -*-

# 动态规划思路， 动态方程： f(n) = f(n-1) + f(n-2)
class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n
        one = 0
        two = 1
        for i in range(n-1):
            now = (one + two) % MOD
            one = two
            two = now
        return two
