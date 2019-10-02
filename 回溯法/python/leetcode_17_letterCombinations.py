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

        def dfs(string, item):
            if len(string) == 0:
                result.append(item)
                return 
        
            for char in self.phone[string[0]]:
                dfs(string[1:], item[:] + char)


        result = []
        if digits:
            dfs(digits, '')
        
        return result