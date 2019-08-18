# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here

        if not array:
            return 0
        pre_maxvalue = 0
        max_value = -0xffffff

        for val in array:
            now_maxvalue = pre_maxvalue + val
            if now_maxvalue < 0:
                pre_maxvalue = 0
            else:
                pre_maxvalue = now_maxvalue
            
            if now_maxvalue > max_value:
                max_value = now_maxvalue

        return max_value


if __name__ == "__main__":
    
    print(Solution().FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2]))
