

# 思路：s(digits[0...n-1]) = letter(digits[0]) + s(digits[1...n-1]) = letter(digits[0]) + letter(digits[1]) + s(digits[2...n-1])

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        self.phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtracking(digits, item):
            if len(digits) == 0:
                result.append(item)
                return 
        
            for word in self.phone[digits[0]]:
                backtracking(digits[1:], item + word)

        result = []
        if digits:
            backtracking(digits, '')
        
        return result