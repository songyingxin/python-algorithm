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