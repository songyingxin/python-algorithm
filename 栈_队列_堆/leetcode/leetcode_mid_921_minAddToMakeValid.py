class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []

        res = 0
        for val in s:
            if val == '(':
                stack.append(val)
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        
        res += len(stack)
        return res