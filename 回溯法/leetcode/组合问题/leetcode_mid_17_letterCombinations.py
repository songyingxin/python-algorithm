class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        n = len(digits)
        help_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(item, start_index):
            if len(item) == n:
                res.append(item)
                return
            
            now_str = help_dict[digits[start_index]]
            for val in now_str:
                tmp_item = item + val
                dfs(item + val, start_index+1)
        
        dfs("", 0)
        return res