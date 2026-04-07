class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = [0] * 26
        a_start = ord('a')
        for val in s:
            s_dict[ord(val)-a_start] += 1
        
        for val in t:
            s_dict[ord(val)-a_start] -= 1
        
        for val in s_dict:
            if val != 0:
                return False
            
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}

        for val in s:
            if val not in s_dict:
                s_dict[val] = 1
            else:
                s_dict[val] += 1
        
        for val in t:
            if val not in s_dict:
                return False
            s_dict[val] -= 1
        
        for key,val in s_dict.items():
            if val != 0:
                return False
        
        return True
