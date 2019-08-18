# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s=''
        self.dict1={}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict1[i]==1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s=self.s+char
        if char in self.dict1:
            self.dict1[char]=self.dict1[char]+1
        else:
            self.dict1[char]=1
