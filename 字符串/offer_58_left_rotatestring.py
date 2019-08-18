# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here

        left = s[:n]
        rigth = s[n:]
        return rigth + left


