"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
"""思路1"""
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result= []
        for char in s:
            if char == ' ':
                result.append('%20')
            else:
                result.append(char)
        return ''.join(result)

print(Solution().replaceSpace('we are '))
