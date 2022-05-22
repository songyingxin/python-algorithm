# -*- coding:utf-8 -*-


# 思想： 用一个栈来模拟这个过程
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
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



