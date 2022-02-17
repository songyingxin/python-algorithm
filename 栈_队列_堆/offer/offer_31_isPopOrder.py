# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        
        stack = []

        for i in pushV:
            stack.append(i)

            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            
        if stack:
            return False
        
        return True



