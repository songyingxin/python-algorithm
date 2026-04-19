

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        n = len(s)

        def dfs(item, start_index):
            if start_index == n:
                res.append(item)
                return
            
            for i in range(start_index+1, n+1):
                sub_str = s[start_index:i]
                if sub_str == sub_str[::-1]:
                    dfs(item+[sub_str], i)
        dfs([], 0)
        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(s, item):
            if not s:
                res.append(item)
                return 

            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], item + [s[:i]])

        dfs(s,[])
        return res



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        #print(dp)
        res = []

        def dfs(i, item):
            if i == n:
                res.append(item)
                return
            for j in range(i, n):
                if dp[i][j]:
                    dfs(j + 1, item + [s[i: j + 1]])

        dfs(0, [])
        return res