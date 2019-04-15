class Solution:
    def isMatch(self, s, p):

        p_ptr = 0
        s_ptr = 0
        while p_ptr < len(p) and s_ptr < len(s):
            
