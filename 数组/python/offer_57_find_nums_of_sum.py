# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here

        left = 0
        right = len(array) - 1

        result = []

        while (left < right):

            if array[left] + array[right] == tsum:
                result = (array[left], array[right])
                break
            
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                left +=1
        
        return result

