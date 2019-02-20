# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        if len(rotateArray)  == 0:
            return None
        
        start_one = rotateArray[0]

        for num in rotateArray[1:]:

            if start_one > num:
                return num
            
            start_one = num
        

        

