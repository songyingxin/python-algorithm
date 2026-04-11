

class Solution:
    def reverseVowels(self, s: str) -> str:

        help_set = ['a','A', 'e','E','i', 'I','o','O','u','U']
        help_set = set(help_set)

        s_list = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s_list[left] in help_set and s_list[right] in help_set:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left += 1
                right -= 1
            if s_list[left] not in help_set:
                left += 1
            if s_list[right] not in help_set:
                right -= 1
        
        return ''.join(s_list)


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
