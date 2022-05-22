# -*- coding:utf-8 -*-


# 思想：   
# push： 直接将元素直接存入 stack1 中
# pop: 如果stack2为空，则将stack1 中元素压入到stack2中，再pop； 如果非空，则直接pop。
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()