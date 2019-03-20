class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        help = {}
        str_list = str.split()

        if len(str_list) != len(pattern):
            return False

        for i in range(len(str_list)):
            if str_list[i] in help.keys():
                if pattern[i] != help[str_list[i]]:
                    return False
            
            elif pattern[i] in help.values():
                return False
            else:
                help[str_list[i] ] = pattern[i]
        
        return True
                
            
if __name__ == "__main__":
    pattern = "abba"
    string = "dog ca cat dog"

    print(Solution().wordPattern(pattern, string))
