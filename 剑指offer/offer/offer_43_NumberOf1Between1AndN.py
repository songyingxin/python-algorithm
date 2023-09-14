# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cnt , i = 0, 1
        while i <= n:
            cnt += n // (i * 10) * i
            cnt += min(max(n %(i*10) - i + 1, 0), i)
            i *= 10
        
        return cnt
