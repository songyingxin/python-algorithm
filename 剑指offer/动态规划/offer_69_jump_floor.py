# -*- coding:utf-8 -*-

# 动态方程：f(n) = f(n-1) + f(n-2)
class Solution:
    def numWays(self, n: int) -> int:
        
        if n == 0:
            return 1
        if n < 3:
            return n
            
        MOD = 10**9 + 7
        one = 1
        two = 1

        for i in range(n-1):
            now = (one + two) % MOD
            one = two
            two = now
        
        return two
