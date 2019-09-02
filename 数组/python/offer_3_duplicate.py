# -*- coding:utf-8 -*-
# 思路1
class Solution:
    def duplicate(self, numbers, duplication):
        help_set = set()
        for val in numbers:
            if val in help_set:
                duplication[0] = val
                return True
            help_set.add(val)
        
        return False
            
# 思路2
class Solution:
    def duplicate(self, numbers, duplication):
        i = 0
        while i < len(numbers):
            if numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                 
                # 注意，此时的交换不能直接采用 numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
                tmp = numbers[i]
                numbers[i], numbers[tmp] = numbers[tmp], numbers[i]
            else:
                i += 1
        return False

# 二分思想
class Solution:
    def duplicate(self, numbers, duplication):

        if not numbers:
            return False
        
        start = 1
        end = len(numbers) - 1

        while start <= end:

            middle = (end - start) // 2 + start
            count = self.count_range(numbers, start, middle)
            if end == start:
                if count > 1:
                    duplication[0] = start
                    return True
                else:
                    break
            if count > middle - start + 1:
                end = middle
            else:
                start = middle + 1
            
        return False

    def count_range(self, numbers, start, end):
        """ 统计 numbers 中处于 [start, end] 之间的个数 """
        if not numbers:
            return 0
        count = 0
        for i in range(len(numbers)):
            if numbers[i] >= start and numbers[i] <= end:
                count += 1

        return count
        
