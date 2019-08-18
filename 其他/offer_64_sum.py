# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def sub_sum(n):
            self.sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        sub_sum(n)
        return self.sum


