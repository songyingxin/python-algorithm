# -*- coding:utf-8 -*-

class ArrayStack:
    def __init__(self, init_size):
        if init_size < 0:
            raise RuntimeError("the init size is too low")
        self.size = init_size
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) == self.size:
            raise IndexError("the array is full")
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


class Queue:
    def __init__(self, init_size):
        self.size = init_size
        self.items = []

    def enqueue(self, item):
        if len(self.items) == self.size :
            raise IndexError("the array is full")
        self.items.append(item)

    def dequeue(self):
        if self.size():
            raise IndexError("the array has no value")
        return self.items.pop(0)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return False


if __name__ == "__main__":

    stack = ArrayStack(-1);

    for i in range(11):
        stack.push(i)
