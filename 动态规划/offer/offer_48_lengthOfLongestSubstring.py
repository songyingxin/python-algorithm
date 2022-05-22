


class Solution:
    def lengthOfLongestSubstring(self , s: str) -> int:
        # write code here
        char2index = {}
        pre = 0
        res = 0
        
        for index in range(len(s)):
            now_char = s[index]
            pre_index = char2index.get(now_char, -1)
            char2index[now_char] = index
            if pre < index - pre_index:
                pre = pre + 1
            else:
                pre = index - pre_index
            res = max(res, pre)
        return res