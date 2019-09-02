class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}  # 已经访问过的字符最近的index
        max_length = 0
        start = 0

        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            used[c] = i
        
        return max_length

