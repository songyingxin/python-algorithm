
# 思路1
class Solution:
    def __init__(self):
        self.max_len = 0  # 最长回文子串最大长度
        self.start = 0  # 最长回文子串起始位置

    def longestPalindrome(self, s: str) -> str:

        s_len = len(s)
        if s_len < 2:
            return s
        
        for k in range(s_len):
            self.long_str(s, k, k, s_len)
            self.long_str(s, k, k+1, s_len)
        
        return s[self.start: self.start + self.max_len]
    
    def long_str(self, s, core1, core2, s_len):
        """
        寻找以 core 1， core2 为回文串中心的最长回文子串
        """
        while core1 >= 0 and core2 < s_len and s[core1] == s[core2]:
            core1 -= 1
            core2 += 1

        if self.max_len < core2 - core1 - 1:
            self.max_len =  core2 - core1 - 1
            self.start = core1 + 1
        
# 思路2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        max_len = 1
        n = len(s)
        start = 0

        for i in range(1, n):
            even = s[i- max_len:i+1]
            odd = s[i-max_len-1:i+1]

            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
            elif i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
        
        return s[start: start + max_len]

# 思路3: 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res


                    



