# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        
        copy = data[:]




        def core(data, copy, start, end):
            if start == end:
                copy[start] = data[start]
                return 0
            
            length = (end - start) // 2

            left = core(copy, data, start, start + length)
            right = core(copy, data, start + length + 1, end)

            
