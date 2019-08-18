class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        string = ['(', '[', '{']
        string_dict = {
            '(': ')', 
            '[': ']',
            '{': '}'
        }

        for val in s:
            if val in string:
                stack.append(val)
            else:
                if not stack or string_dict[stack[-1]]!= val:
                    return False
                stack.pop()
        
        if stack:
            return False
        
        return True
