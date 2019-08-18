# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 and m < 1:
            return -1
        
        last = 0
        for i in range(2, n+1):
            last = (last + m) % i
        
        return last


