class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.help = []

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.data) > 1:
            self.help.append(self.data.pop(0))
        
        result = self.data.pop(0)
        self.help, self.data = self.data, self.help
        return result

    def top(self):
        """
        Get the top element.
        """
        while len(self.data) > 1:
            self.help.append(self.data.pop(0))
        result = self.data[0]
        self.help.append(self.data.pop(0))
        self.help, self.data = self.data, self.help
        return result


    def empty(self):
        """
        Returns whether the stack is empty.
        """
        if not self.data:
            return True
        
        return False
