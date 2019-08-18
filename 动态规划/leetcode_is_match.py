
# 递归方法，过不了
class Solution:
    # s, pattern都是字符串
    def isMatch(self, s, pattern):
        # write code here

        # 0. 二者同时匹配结束
        if not s and not pattern:
            return True

        # 1. pattern已经结束但 字符串并没有完全匹配
        if s and not pattern:
            return False
        
        # 当字符串结束，pattern 未结束时，还需要匹配

        # 当 pattern 第二个字符为 *时
        if len(pattern) > 1 and pattern[1] == '*':
            # s与pattern 第一个字符匹配
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.isMatch(s, pattern[2:]) or self.isMatch(s[1:], pattern[2:]) or self.isMatch(s[1:], pattern)
            else:
                return self.isMatch(s, pattern[2:])

        if len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0]):
            return self.isMatch(s[1:], pattern[1:])

        return False
    

# 递归，精简代码
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


# 动态规划
class Solution(object):
    def isMatch(self, text, pattern) -> bool:
        memo = dict() # 备忘录
        def dp(i, j):
            if (i, j) in memo: 
                return memo[(i, j)]

            if j == len(pattern): 
                return i == len(text)

            first = i < len(text) and pattern[j] in {text[i], '.'}
            
            if j <= len(pattern) - 2 and pattern[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)
                
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)



    

    


