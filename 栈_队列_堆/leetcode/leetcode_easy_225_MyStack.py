
# push： 直接将元素存入data中
# pop： 将data 中的元素依次 pop到help中，直至data中只剩下一个元素， 然后弹出该元素， data， help互换

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.help_queue = []

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue) > 1:
            self.help_queue.append(self.queue.pop(0))

        result = self.queue.pop(0)
        self.queue = self.help_queue
        self.help_queue = []
        return result

    def top(self):
        """
        Get the top element.
        """
        if not self.queue:
            return 
        return self.queue[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        if not self.queue:
            return True

        return False
