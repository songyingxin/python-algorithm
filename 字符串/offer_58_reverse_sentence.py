# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        strings = s.split(' ')
        return ' '.join(strings[::-1])


if __name__ == "__main__":
    
    print(Solution().ReverseSentence(''))