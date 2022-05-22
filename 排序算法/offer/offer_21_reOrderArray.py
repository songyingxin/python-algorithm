# -*- coding:utf-8 -*-


# 思路1： 采用额外数组，第一次遍历奇数存储到数组，第二次遍历偶数存储到数组中
class Solution:
    def reOrderArray(self , array ):
        # write code here
        res = []
        for num in array:
            if num % 2 != 0:
                res.append(num)
        
        for num in array:
            if num % 2 == 0:
                res.append(num)
        return res

# 思路2： 直接采用 python 中的双向队列
from collections import deque

class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = deque()
        x = len(array)
        for i in range(x):
            if array[x-i-1] % 2 != 0:
                odd.appendleft(array[x-i-1])
            if array[i] % 2 == 0:
                odd.append(array[i])
        return list(odd)

# 思路3： 采用 odd_index 保存奇数要保存的位置，然后遍历数组，将odd_index 到 index 的数据全都向后移一位
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd_index = 0
        
        for index in range(len(array)):
            if array[index] % 2 != 0:
                tmp = array[index]
                for i in range(index-1, odd_index-1, -1):
                    array[i+1] = array[i]
                array[odd_index] = tmp
                odd_index += 1
        return array