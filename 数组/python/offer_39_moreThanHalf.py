# -*- coding:utf-8 -*-

# 思路2
import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0

        res = numbers[0]
        times = 1

        for number in numbers[1:]:
            if times == 0:
                res = number
                times = 1
            elif number == res:
                times += 1
            else:
                times -= 1

        return res if collections.Counter(numbers)[res] * 2 > len(numbers) else 0



    
