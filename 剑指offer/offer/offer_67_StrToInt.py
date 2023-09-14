# -*- coding:utf-8 -*-

# https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&tqId=11202&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        index = 0
        if s[0] == '-' or s[0] == '+':
            index += 1

        result = 0
        for i in range(index, len(s)):
            if s[i] < '0' or s[i] > '9':
                return 0
            result = result * 10 + int(s[i])

        if s[0] == '-':
            result = -result

        return result
