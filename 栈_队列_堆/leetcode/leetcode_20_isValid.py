class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        left_char =  ['(', '[', '{']
        string_dict = {
            ')': '(', 
            ']': '[',
            '}': '{'
        }

        for _char in s:
            if _char in left_char:
                stack.append(_char)
            else:
                if stack and string_dict[_char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True