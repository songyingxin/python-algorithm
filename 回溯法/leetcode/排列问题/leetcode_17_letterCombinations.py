

# 思路：s(digits[0...n-1]) = letter(digits[0]) + s(digits[1...n-1]) = letter(digits[0]) + letter(digits[1]) + s(digits[2...n-1])

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
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

        def dfs(now_digits, item):
            if not now_digits:
                res.append(item)
                return
            
            now_str = help_dict[now_digits[0]]
            for val in now_str:
                tmp_item = item + val
                dfs(now_digits[1:], tmp_item)
        
        dfs(digits, "")
        return res