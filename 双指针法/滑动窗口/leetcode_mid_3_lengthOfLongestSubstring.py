class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        help_dict = {}
        max_len = 0

        left = 0
        for i,val  in enumerate(s):
            if val in help_dict and left <= help_dict[val]:
                left = help_dict[val]+1

            now_len = i-left+1
            max_len = max(now_len, max_len)
            help_dict[val] = i
        
        return max_len