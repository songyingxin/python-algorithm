class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0 
        pre_dict = {} # 已经访问过的字符最新的index

        start = 0  # 记录当前字符串的开始位置

        for i, v in enumerate(s):
            if v in pre_dict and start <=pre_dict[v]:
                start = pre_dict[v] + 1
            
            max_length = max(max_length, i-start+1)
            pre_dict[v] = i
        return max_length


