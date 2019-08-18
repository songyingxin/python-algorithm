# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0

        one = 1
        two = 2
        for i in range(number-1):
            one, two = two, one + two

        return one
