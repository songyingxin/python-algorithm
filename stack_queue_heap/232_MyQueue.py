class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.help = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.help:
            while self.data:
                self.help.append(self.data.pop())
        return self.help.pop()

    def peek(self):
        """
        Get the front element.
        """
        if not self.help:
            while self.data:
                self.help.append(self.data.pop())

        return self.help[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        if not self.data and not self.help:
            return True

        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
