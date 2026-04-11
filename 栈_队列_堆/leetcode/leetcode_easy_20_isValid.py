class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        help_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for val in s:
            if val in help_dict:
                stack.append(val)
            else:
                if not stack:
                    return False
                tmp = stack.pop()
                if help_dict[tmp] != val:
                    return False
        if stack:
            return False
        return True
        