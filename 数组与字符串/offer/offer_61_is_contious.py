# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
            
        numbers = sorted(numbers)
        times_0 = numbers.count(0)
        numbers = numbers[times_0:]

        vacancy_nums = 0
        for i in range(0, len(numbers)-1):
            if numbers[i+1] == numbers[i]:
                return False
            vacancy_nums += numbers[i+1] - numbers[i] - 1
        
        if vacancy_nums > times_0:
            return False
        else:
            return True

        


