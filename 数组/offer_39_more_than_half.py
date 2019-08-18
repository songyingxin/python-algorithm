# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here

        result = {}
        judge = len(numbers) // 2

        for number in numbers:
            if number not in result.keys():
                result[number] = 1
            else:
                result[number] += 1
        
        for key, value in result.items():
            if value > judge:
                return key
        
        return 0



    
