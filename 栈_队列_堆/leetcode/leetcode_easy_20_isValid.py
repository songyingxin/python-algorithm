class Solution:
    def isValid(self, s: str) -> bool:

        help_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for val in s:
            if val in help_dict:
                stack.append(val)
            else:
                if stack and help_dict[stack[-1]] == val:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True