# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here

        if not sequence:
            return False
        
        if len(sequence) == 1:
            return True
        
        length = len(sequence)
        root = sequence[-1]
        i = 0

        while sequence[i] < root:
            i = i + 1
        
        for j in range(i, length-1):
            if sequence[j] < root:
                return False
        
        left_s = sequence[:i]
        right_s = sequence[i:length-1]

        left = self.VerifySquenceOfBST(left_s) if left_s else True
        right = self.VerifySquenceOfBST(right_s) if right_s else True

        return left and right

