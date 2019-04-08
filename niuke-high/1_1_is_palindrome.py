class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = str(x)
        left = 0
        right = len(x) -1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True







x = 10
print(Solution().isPalindrome(x))
