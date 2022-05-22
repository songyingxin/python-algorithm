


class Solution:
    def FirstNotRepeatingChar(self , str: str) -> int:
        # write code here

        char2times = {}
        for index, _char in enumerate(str):  
            if _char in char2times:
                char2times[_char].append(index)
            else:
                char2times[_char] = [index]
        
        for _char, times in char2times.items():
            if len(times) == 1:
                return times[0]
        
        return -1