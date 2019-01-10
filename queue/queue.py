# -*- coding:utf-8 -*-
#!/usr/bin/env python

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
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
