# 思路1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        str_x = str(x)

        for i in range(len(str_x)//2):
            if str_x[i] != str_x[-(i+1)]:
                return False
        
        return True

# 思路1
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = str(x)
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True

# 思路2
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        help_val = 1

        # 找到比 n 小的第一个 10 的倍数，如 n= 101， 则 helo_val = 100
        while x // help_val >= 10:
            help_val *= 10
        
        while x != 0:
            if x // help_val != x % 10: # 第一位与最后一位比较
                return False
            
            x = (x % help_val) // 10  # 去除首位与尾位
            help_val //= 100
        
        return True


