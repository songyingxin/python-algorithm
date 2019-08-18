class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_data = []
        self.stack_min = []

    def push(self, x):
        self.stack_data.append(x)
        if self.stack_min:
            self.stack_min.append(min(x, self.stack_min[-1]))
        else:
            self.stack_min.append(x)

    def pop(self):
        self.stack_data.pop()
        self.stack_min.pop()

    def top(self):
        if self.stack_data:
            return self.stack_data[-1]
        else:
            return None

    def getMin(self):
        if self.stack_min:
            return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
