# -*- coding:utf-8 -*-

# 思路： 定义 
# C[i] = A[0] * ... * A[i-1], 
# D[i] = A[i+1] * ... * A[n-1]， 那么则有： 
# C[i] = C[i-1] * A[i-1]， D[i] = D[i+1] * A[i+1]， 
# 最终的 B[i] = C[i] * D[i]

class Solution:
    def multiply(self, A):
        # write code here

        C = [1 for i in range(len(A))]
        D = [1 for i in range(len(A))]

        for i in range(1, len(A)):
            C[i] = C[i-1] * A[i-1]
        
        for i in range(0, len(A)-1)[::-1]:
            D[i] = D[i+1] * A[i+1]
        
        B = [C[i] * D[i] for i in range(len(A))]

        return B


