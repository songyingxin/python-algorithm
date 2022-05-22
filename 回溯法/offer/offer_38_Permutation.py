# -*- coding:utf-8 -*-
class Solution:

    def Permutation(self, ss):
        # write code here
        res = set()

        def back_track(string, path):
            if string == '':
                res.add(path)
            else:
                for i in range(len(string)):
                    back_track(string[:i]+string[i+1:], path + string[i])
        back_track(ss, '')
        return list(res)


        
        
