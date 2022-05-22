class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        this_str = ''
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char.isalpha():
                this_str += char
            elif char == '[':
                stack.append((this_str, num))
                this_str, num = '', 0
            else:
                last_str, this_num = stack.pop()
                this_str = last_str + this_num * this_str

        return this_str
