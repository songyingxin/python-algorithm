# -*- coding:utf-8 -*-

# 思路1: 找到第一个出现逆序的数字即可
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        pre = rotateArray[0]

        for val in rotateArray[1:]:
            if pre > val:
                return val
            pre = val
        
        return rotateArray[0]


# 思路2： 二分查找，找到第一个逆序的数字.
# 

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        left = 0
        right = len(rotateArray) - 1

        while left < right:
            mid = (left + right) // 2
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                right -= 1
        return rotateArray[left]
            

