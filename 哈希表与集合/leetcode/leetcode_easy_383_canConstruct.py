class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        help_dict = {}

        for val in magazine:
            if val in help_dict:
                help_dict[val] += 1
            else:
                help_dict[val] = 1
        
        for val in ransomNote:
            if val not in help_dict:
                return False
            
            if help_dict[val] <= 0:
                return False
            
            help_dict[val] -= 1
        
        return  True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        help_dict = [0] * 52
        a_start = ord('a')

        for val in magazine:
            help_dict[ord(val)-a_start] += 1
        
        for val in ransomNote:
            help_dict[ord(val)-a_start] -= 1
        
        for val in help_dict:
            if val < 0:
                return False
        
        return True