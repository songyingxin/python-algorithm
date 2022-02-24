# -*- coding:utf-8 -*-

# 思路1
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        
        if exponent == 0:
            return 1
        

        result = 1
        for i in range(abs(exponent)):
            result *= base
        
        if exponent < 0:
            result = 1 / result
        
        return result
        
        