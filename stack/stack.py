# -*- coding:utf-8 -*-

""" 采用 list 对列表进行实现 """
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        """ 查看栈顶元素 """
        if not self.is_empty():
            return self.items[-1]
        else:
            return False

    def size(self):
        return len(self.items)
