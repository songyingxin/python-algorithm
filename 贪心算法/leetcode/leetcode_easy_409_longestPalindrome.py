class Solution:
    def longestPalindrome(self, s: str) -> int:

        help_dict = {}
        for val in s:
            if val in help_dict:
                help_dict[val] += 1
            else:
                help_dict[val] = 1
        
        res = 0
        for key,val in help_dict.items():
            res += val//2 * 2

        if res == len(s):
            return res
        else:
            return res + 1