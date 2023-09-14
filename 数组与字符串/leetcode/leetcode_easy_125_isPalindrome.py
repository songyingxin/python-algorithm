
# 思路
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
