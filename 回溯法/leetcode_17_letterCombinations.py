class Solution:

    def __init__(self):

        self.dict_arr = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.result = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        item = ''
        self.dfs(digits, item)
        return self.result

    
    def dfs(self, string, item):
        if len(string) == 0:
            self.result.append(item)
            return 
        
        for char in self.dict_arr[string[0]]:
            self.dfs(string[1:], item[:] + char)