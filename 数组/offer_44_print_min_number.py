# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here

        if not numbers:
            return ""
        
        lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        array = sorted(numbers, cmp=lmb)
        return ''.join([str(i) for i in array])
