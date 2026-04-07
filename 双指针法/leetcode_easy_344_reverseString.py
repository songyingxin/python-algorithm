class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        for i in range(s_len//2):
            s[i], s[s_len-i-1] = s[s_len-i-1], s[i]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:
            s[left],s[right] = s[right], s[left]
            left += 1
            right -= 1
        