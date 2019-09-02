# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here

        # 0. 二者同时匹配结束
        if len(s) == 0 and len(pattern) == 0:
            return True
        
        # 1. pattern已经结束但 字符串并没有完全匹配
        if len(s) > 0 and len(pattern) == 0:
            return False
        
        # 当 pattern 第二个字符为 *时
        if len(pattern) > 1 and pattern[1] == '*':
            # s与pattern 第一个字符匹配
            if len(s) > 0 and (s[0] == pattern[0]  or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        
        if len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0]) :
            return self.match(s[1:], pattern[1:])
        
        return False