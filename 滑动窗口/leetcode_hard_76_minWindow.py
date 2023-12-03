class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def match(t_dict, s_dict):
            for i in range(len(t_dict)):
                if s_dict[i] < t_dict[i]:
                    return False
            
            return True
        
        s_dict = [0] * 58
        t_dict = [0] * 58

        left = 0
        right = 0
        min_len = float('inf')
        ord_A = ord('A')
        res = ''
        for val in t:
            t_dict[ord(val) - ord_A] += 1
        
        while right < len(s):
            right_index = ord(s[right])-ord_A
            s_dict[right_index] += 1

            while match(t_dict, s_dict):
                if right-left+1 < min_len:
                    min_len = right-left+1
                    res = s[left:right+1]
                
                left_index = ord(s[left]) - ord_A
                s_dict[left_index] -= 1
                left += 1
            
            right += 1
        
        return res