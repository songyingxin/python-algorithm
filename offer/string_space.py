# -*- coding:utf-8 -*-


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # 思路1
        result= []
        for char in s:
            if char == ' ':
                result.append('%20')
            else:
                result.append(char)
        return ''.join(result)

