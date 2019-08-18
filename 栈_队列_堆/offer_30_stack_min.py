# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
         self.min_stack = []
         self.core_stack = []

    def push(self, node):
        # write code here
        self.core_stack.append(node)

        if not self.min_stack or node < self.min_stack[-1]:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        # write code here
        self.core_stack.pop()
        self.min_stack.pop()

    def top(self):
        # write code here
        return self.core_stack[-1]

    def min(self):
        # write code here
        return self.min_stack[-1]
