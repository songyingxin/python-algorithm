

class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for val in s:
            if stack and val == stack[-1]:
                stack.pop()
            else:
                stack.append(val)
        
        return ''.join(stack)