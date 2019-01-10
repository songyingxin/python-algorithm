# -*- coding:utf-8 -*-

"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

Input: [1,2,3,4,5]
Output: [120, 60, 40, 30, 24]
"""


class Solution:
    def multiply(self, A):
        # write code here
        B = list(range(len(A)))
        for i in range(len(A)):
            new_array = A[:i]
            new_array.extend(A[i+1:])
            value = 1
            for j in new_array:
                value *= j
            B[i] = value
        return B

a = Solution()
A = [1,2,3,4,5]
b = a.multiply(A)
print(b)
