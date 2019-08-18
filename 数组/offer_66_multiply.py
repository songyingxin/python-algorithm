# -*- coding:utf-8 -*-
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


