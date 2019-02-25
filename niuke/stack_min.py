# -*- coding:utf-8 -*-


class StackMin1:
    def __init__(self):
        self.stack_data = []
        self.stack_min = []

    def push(self, new_num):
        if not self.stack_min:
            self.stack_min.append(new_num)
        elif new_num <= self.stack_min[-1]:
            self.stack_min.append(new_num)

        self.stack_data.append(new_num)

    def pop(self):
        if not self.stack_data:
            raise  RuntimeError("you stack is Empty")
        value = self.stack_data.pop()
        if value == self.get_min():
            self.stack_min.pop()
        return value

    def top(self):
        """ 查看栈顶元素 """
        if not self.is_empty():
            return self.stack_data[-1]
        else:
            return False

    def get_min(self):
        """ 返回栈的最小值 """
        if not self.stack_min:
            raise RuntimeError("your stack is Empty")
        return self.stack_min[-1]

    def size(self):
        return len(self.stack_data)

    def is_empty(self):
        return self.stack_data == []


if __name__ == "__main__":
    
    