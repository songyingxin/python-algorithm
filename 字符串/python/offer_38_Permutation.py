# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.res = set()

    def Permutation(self, ss):
        # write code here
        if len(ss) <= 0:
            return []

        def perm(string, path):
            if string == '':
                self.res.add(path)
            else:
                for i in range(len(string)):
                    perm(string[:i]+string[i+1:], path + string[i])
        perm(ss, '')
        return sorted(list(self.res))


        
        
