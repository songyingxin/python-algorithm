class Solution:
    def reverseVowels(self, s: str) -> str:

        result = list(s)
        left = 0
        right = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while left < right:
            if result[left] in vowels:
                while result[right] not in vowels:
                    right -= 1
                result[left], result[right] = result[right], result[left]
                right -= 1
            left += 1
        return ''.join(result)
