class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        res = []
        n = len(s)

        def dfs(item, start_index):
            if len(item) == n:
                res.append(item)
                return
            
            c = s[start_index]
            if c.isdigit():
                item = item + s[start_index]
                dfs(item, start_index+1)
            else:
                dfs(item+c.lower(), start_index+1)
                dfs(item+c.upper(), start_index+1)
        
        dfs('', 0)
        return res